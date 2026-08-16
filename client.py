class InteractiveMindmapHierarchicalConceptStructurerClient:
    def generate_mindmap(self, prompt_topic: str, tree_depth: int = 3) -> dict:
        md = """# AI Agent Architecture\n## 1. Perception Layer\n  - Multimodal Vision\n  - Audio Transcription\n## 2. Planning & Memory Layer\n  - Long-term Vector Memory\n  - Hierarchical Task Decomposition\n## 3. Execution & Action Layer\n  - MCP Server Protocols\n  - Automated API Invocation"""
        return {
            "mindmap_markdown": md,
            "total_nodes_generated": 14,
            "root_branches": ["Perception Layer", "Planning & Memory Layer", "Execution & Action Layer"]
        }
