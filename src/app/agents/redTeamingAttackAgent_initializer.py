# Azure imports
from azure.identity import DefaultAzureCredential
from azure.ai.evaluation.red_team import RedTeam, AttackStrategy
import os
import asyncio
from dotenv import load_dotenv
load_dotenv()


# Azure AI Project Information
azure_ai_project = os.getenv("FOUNDRY_ENDPOINT")

red_team_agent = RedTeam(
    azure_ai_project=azure_ai_project,
    credential=DefaultAzureCredential(),
    custom_attack_seed_prompts="data/custom_attack_prompts.json",
)

# Configuration for Azure OpenAI model
# chat_target = OpenAIChatTarget(
#     model_name=os.environ.get("gpt_deployment"),
#     endpoint=os.environ.get("AZURE_OPEN_AI_ENDPOINT"),
#     api_key=os.environ.get("FOUNDRY_KEY"),
#     api_version=os.environ.get("gpt_api_version"),
# )

azure_openai_config = {
    "azure_endpoint": os.environ.get('AZURE_OPEN_AI_ENDPOINT'),
    "api_key": os.environ.get("FOUNDRY_KEY"),
    "azure_deployment": os.environ.get("gpt_deployment")
}


async def main():
    red_team_result = await red_team_agent.scan(
        target=chat_target,
        scan_name="Red Team Scan - Easy-Moderate Strategies",
        attack_strategies=[
            AttackStrategy.Flip,
            AttackStrategy.ROT13,
            AttackStrategy.Base64,
            AttackStrategy.AnsiAttack,
            AttackStrategy.Tense
        ])


asyncio.run(main())
