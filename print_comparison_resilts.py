import json 

def print_results(file = "model_comparison_results.json"):

    with open(file, 'r') as f:
        data = json.load(f)

    count = 1
    output_filename = "results_quesitions.txt"

    with open(output_filename, 'w') as outfile:

        for n in range(len(data["Question"])):
            key = f"question_{n+1}"
            question = data["Question"][key]
            trained = data["trained_model"][key]
            untrained = data["untrained_model"][key]

            grade = question.split(" ")[2]
            trained = trained.split("<|im_start|>assistant\n")[1]
            untrained = untrained.split("<|im_start|>assistant\n")[1]

            outfile.write(f"Question Number: {count}\n")
            outfile.write(f"Grade Level: {grade}\n")
            outfile.write(f"Question: {question}\n")
            outfile.write(f"Answer 1: {trained}\n")
            outfile.write(f"Answer 2: {untrained}\n")
            outfile.write("Choice:\n\n")

            count += 1

if __name__ == "__main__":
    print_results()