import yaml

def parse_workflow(yaml_file):
    with open(yaml_file, 'r') as file:
        workflow = yaml.safe_load(file)
        jobs = workflow.get('jobs', {})
        num_jobs = len(jobs)

        num_steps = 0
        for job in jobs.values():
            steps = job.get('steps', [])
            num_steps += len(steps)

        return num_jobs, num_steps

if __name__ == "__main__":
    yaml_file = input("Enter the path to the YAML file: ")

    try:
        num_jobs, num_steps = parse_workflow(yaml_file)
        print(f"Number of jobs: {num_jobs}")
        print(f"Number of steps: {num_steps}")
    except FileNotFoundError:
        print("File not found. Please provide a valid YAML file path.")
    except yaml.YAMLError as e:
        print(f"Error parsing YAML file: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
