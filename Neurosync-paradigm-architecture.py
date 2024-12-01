import os
from amanaknows import AmanaknowsModel

# Utility: Ensure a directory exists
def ensure_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

# Utility: Save results to a file
def save_results(version, results):
    output_file = f"results_{version}.json"
    ensure_directory("results")
    with open(os.path.join("results", output_file), 'w') as file:
        json.dump(results, file, indent=4)
    print(f"Results for version {version} saved to results/{output_file}")

# Configuration dictionary for all versions
CONFIG = {
    "1.0": {
        "model_params": {
            "version": "1.0",
            "dynamic_loading": True
        },
        "phrases_to_test": [
            "bank of a river",
            "financial bank",
            "light beam",
            "laser beam"
        ]
    },
    "2.0": {
        "model_params": {
            "version": "2.0",
            "dynamic_loading": True
        },
        "dataset": [
            {"input": "parallel data A", "variant": "reality X"},
            {"input": "parallel data B", "variant": "reality Y"}
        ]
    },
    "3.0": {
        "model_params": {
            "version": "3.0",
            "dynamic_loading": True
        },
        "input_sets": [
            ["thought pattern A", "response pattern B"],
            ["resonance input X", "resonance input Y"]
        ]
    }
}

# Function: Analyze Semantic Conflation
def analyze_semantic_conflation(model, phrases):
    results = {}
    for phrase in phrases:
        output = model.analyze_phrase(phrase)
        results[phrase] = output
    return results

# Function: Test Neural Confluent Systems
def test_neural_confluence(model, dataset):
    results = []
    for data in dataset:
        output = model.test_confluence(data)
        results.append(output)
    return results

# Function: Test Resonance in Consciousness
def test_resonance(model, inputs):
    patterns = {}
    for input_set in inputs:
        pattern = model.detect_resonance(input_set)
        patterns[str(input_set)] = pattern
    return patterns

# Main Multiversal Executor
def execute_project(version):
    # Load version-specific configuration
    if version not in CONFIG:
        raise ValueError(f"Version {version} configuration not found.")
    config = CONFIG[version]

    # Initialize Amanaknows model
    model = AmanaknowsModel(config["model_params"])

    # Execute tasks based on version
    results = {}
    if version == "1.0":
        results = analyze_semantic_conflation(model, config["phrases_to_test"])
    elif version == "2.0":
        results = test_neural_confluence(model, config["dataset"])
    elif version == "3.0":
        results = test_resonance(model, config["input_sets"])
    else:
        raise ValueError(f"Unsupported version {version}")

    # Save results
    save_results(version, results)

# Entry Point
if __name__ == "__main__":
    print("Dynamic Multiversal Project Manager")
    print("Available Versions: 1.0 (Semantic Conflation), 2.0 (Neural Confluence), 3.0 (Resonance Testing)")
    
    version = input("Enter the version to execute (e.g., 1.0): ").strip()
    try:
        execute_project(version)
    except Exception as e:
        print(f"Error executing project version {version}: {e}")
