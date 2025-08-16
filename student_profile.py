from agents import Agent, Runner, RunContextWrapper, function_tool
from connection import config
from pydantic import BaseModel
import asyncio
import rich

# 📘 Exercise: 02 STUDENT PROFILE CONTEXT

# 🏫 Class for context
class StudentProfile(BaseModel):
    student_id: str | int
    student_name: str
    current_semester: int
    total_courses: int

# 👨‍🎓 Student profile 
student = StudentProfile(
    student_id="STU-456",
    student_name="Muhammad Imad",
    current_semester=4,
    total_courses=5
)

# 🛠️ Function tool
@function_tool
def student_info(wrapper: RunContextWrapper[StudentProfile]):
    student = wrapper.context
    return (
        f"✨ [yellow]Student Profile Information[/ yellow] ✨\n\n"
        f"🆔 [cyan]Student ID:[/cyan] {student.student_id}\n"
        f"👤 [green]Student Name:[/green] {student.student_name}\n"
        f"📘 [magenta]Current Semester:[/magenta] {student.current_semester}\n"
        f"📊 [blue]Total Courses:[/blue] {student.total_courses}\n"
        f"✅ [green]Student profile retrieved successfully![/green]"
    )

# 🤖 Main Agent
Student_agent = Agent(
    name="Info Provider",
    instructions="""
🎓 You are an Academic Records Assistant.  
📌 Your role is to provide complete student profile details using the student_info tool.  
✨ Always present the output in a well-structured way, with colors, highlights, and emojis for better readability.  
""",
    tools=[student_info]
)

# 🚀 Main function
async def main():
    prompt1 = "Show me all the academic information for the student."
    result = await Runner.run(
        Student_agent,
        prompt1,
        run_config=config,
        context=student
    )
    
    # ✅ Rich formatting render karna (direct print)
    rich.print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
