import yaml

def parse_conda_env(yaml_file, output_file):
    with open(yaml_file, 'r') as file:
        env = yaml.safe_load(file)
        with open(output_file, 'w') as outfile:
            for dep in env['dependencies']:
                # Check if dependency is a pip list
                if isinstance(dep, dict) and 'pip' in dep:
                    for pip_dep in dep['pip']:
                        outfile.write(pip_dep + '\n')

parse_conda_env('environment.yml', 'requirements.txt')
