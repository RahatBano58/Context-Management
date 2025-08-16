from agents import Agent, Runner, RunContextWrapper, function_tool
from connection import config
from pydantic import BaseModel
import asyncio
import rich

# Exercise 03: LIBRARY BOOK CONTEXT

# Class for context
class LibraryBook(BaseModel):
    book_id: str | int
    book_title: str
    author_name: str
    is_available: bool

# Library Book
library_book = LibraryBook(
    book_id = "BOOK-123",
    book_title = "Python Programming",
    author_name = "John Smith",
    is_available = True
)

@function_tool
def Library_Info(wrapper: RunContextWrapper[LibraryBook]):
    book = wrapper.context
    return(
        f"✨ [yellow]Library Book Information[/yellow] ✨\n\n"
        f"🔖 [cyan]Book ID:[/cyan] {book.book_id}\n"
        f"📘 [green]Book Title:[/green] {book.book_title}\n"
        f"👨‍🏫 [magenta]Author:[/magenta] {book.author_name}\n"
        f"📚 [green]Is Available:[/green] {book.is_available}\n"
    )

# Main Agent
book_agent = Agent(
    name = "Assistant Agent",
    instructions = 
    """
    📚 You are a smart and friendly Library Assistant Agent.  
    🔍 Your role is to provide clear, accurate, and well-formatted information about library books.  
    ✨ Always use the Library_Info tool when answering queries.  
    🎨 Present details with proper colors, emojis, and formatting to make responses attractive and easy to read.
    """,
    tools = [Library_Info]
)

async def main():
    prompt = "Who is the author of the python programming?"
    result = await Runner.run(
        book_agent,
        prompt,
        run_config = config,
        context = library_book
    )
    rich.print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())