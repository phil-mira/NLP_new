import json 

def print_results(file = "model_comparison_results.json"):
    """
    This function converts the outputs of the models to a format that is suitable
    for marking by an external examiner. It then creates text files for each of the 
    comparisons to be performed. "a" files are for omparisons between the model trained 
    all the data and the base model while "b" files are for comparisons between models trained
    on subsets of the data and the base model. Questions for the primary grades are seperated 
    as they have been assessed by an external reviewer. 

    Args:
        file - the input results file as a json 
    
    """

    with open(file, 'r') as f:
        data = json.load(f)

    count = 1
    primary_filename_a = "results_quesitions_gina_a.txt"
    all_filename_a = "results_questions_full_a.txt"

    primary_filename_b = "results_questions_gina_b.txt"
    all_filename_b = "results_questions_full_b.txt"


    for n in range(len(data["Question"])):
        key = f"question_{n+1}"
        question = data["Question"][key]
        trained = data["trained_model"][key]
        untrained = data["untrained_model"][key]
        experts = data["experts_model"][key]

        grade = question.split(" ")[2]
        trained = trained.split("<|im_start|>assistant\n")[1]
        untrained = untrained.split("<|im_start|>assistant\n")[1]
        experts = experts.split("<|im_start|>assistant\n")[1]

        # Seperate out the questions for primary school children
        if n % 3 == 0: 
            with open(primary_filename_a, 'a') as outfile:
                outfile.write(f"Question Number: {count}\n")
                outfile.write(f"Grade Level: {grade}\n")
                outfile.write(f"Question: {question}\n")
                outfile.write(f"Answer 1: {trained}\n")
                outfile.write(f"Answer 2: {untrained}\n")
                outfile.write("Choice:\n\n\n")

            with open(primary_filename_b, 'a') as outfile:
                outfile.write(f"Question Number: {count}\n")
                outfile.write(f"Grade Level: {grade}\n")
                outfile.write(f"Question: {question}\n")
                outfile.write(f"Answer 1: {experts}\n")
                outfile.write(f"Answer 2: {untrained}\n")
                outfile.write("Choice:\n\n\n")
            

        else: 
            with open(all_filename_a, 'a') as outfile:
                outfile.write(f"Question Number: {count}\n")
                outfile.write(f"Grade Level: {grade}\n")
                outfile.write(f"Question: {question}\n")
                outfile.write(f"Answer 1: {trained}\n")
                outfile.write(f"Answer 2: {untrained}\n")
                outfile.write("Choice:\n\n\n")

            with open(all_filename_b, 'a') as outfile:
                outfile.write(f"Question Number: {count}\n")
                outfile.write(f"Grade Level: {grade}\n")
                outfile.write(f"Question: {question}\n")
                outfile.write(f"Answer 1: {experts}\n")
                outfile.write(f"Answer 2: {untrained}\n")
                outfile.write("Choice:\n\n\n")
            

        count += 1

if __name__ == "__main__":
    print_results()