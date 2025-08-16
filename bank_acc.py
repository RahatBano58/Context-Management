from agents import Agent, Runner, RunContextWrapper, function_tool
from connection import config
from pydantic import BaseModel
import rich
import asyncio

# 🎯 Exercise : 01 BANK ACCOUNT CONTEXT

# 🏦 Class for context
class BankAccount(BaseModel):
    account_number: int | str
    customer_name: str
    account_balance: float
    account_type: str

# 👩‍💼 Account holder profile
bank_account = BankAccount(
    account_number="ACC-789456",
    customer_name="Rahat Bano",
    account_balance=75500.50,
    account_type="Savings"
)

# 🛠️ Function tool
@function_tool
def Bank_info(wrapper: RunContextWrapper[BankAccount]):
    account = wrapper.context
    return (
        f"✨ [yellow]Here is your Bank Account Info:[/yellow] ✨\n\n"
        f"🔢 [green]Account Number:[/green] {account.account_number}\n"
        f"👤 [cyan]Customer Name:[/cyan] {account.customer_name}\n"
        f"💰 [magenta]Account Balance:[/magenta] PKR {account.account_balance:,.2f}\n"
        f"🏦 [blue]Account Type:[/blue] {account.account_type}\n"
    )

# 🤖 Main Agent
Main_agent = Agent(
    name="Info Agent",
    instructions="""
    📌 You are the Main Agent.
    🏦 Your job is to fetch and display bank account details using the Bank_info tool.
    ✨ Always format the response neatly with colors, highlights, and emojis.  
    """,
    tools=[Bank_info]
)

# 🚀 Main function
async def main():
    prompt_1 = "Give me complete my bank account information."
    result = await Runner.run(
        Main_agent,
        prompt_1,
        run_config=config,
        context=bank_account
    )
    rich.print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
