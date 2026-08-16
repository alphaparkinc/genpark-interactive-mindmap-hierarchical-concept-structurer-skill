from client import InteractiveMindmapHierarchicalConceptStructurerClient

def main():
    client = InteractiveMindmapHierarchicalConceptStructurerClient()
    res = client.generate_mindmap("AI Agent Architecture", 3)
    print(f"Nodes Generated: {res['total_nodes_generated']}")
    print("Branches:", res["root_branches"])
    print("\nMindmap Markdown:")
    print(res["mindmap_markdown"])

if __name__ == "__main__":
    main()
