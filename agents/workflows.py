from adk.agents import Sequential, Parallel
from agents.tools.vector_search import VectorSearchTool
from agents.tools.generate import GenerateTool

# Example composite workflows

def baseline_workflow():
    return Sequential(steps=[
        ("retrieve", VectorSearchTool(k=10)),
        ("generate", GenerateTool(model="gemma3:270m"))
    ])

def multi_source_workflow():
    return Sequential(steps=[
        ("parallel_retrieval", Parallel(steps=[
            ("catalog", VectorSearchTool(k=8)),
            ("policies", VectorSearchTool(k=8)),
        ])),
        ("generate", GenerateTool(model="gemma3:270m"))
    ])
