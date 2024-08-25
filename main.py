from secret_santa import SecretSanta

if __name__ == "__main__":
    employees_file = 'employees.csv'
    previous_assignment_file = 'previous_assignments.csv'
    output_file = 'new_assignments.csv'
    
    try:
        secret_santa = SecretSanta(employees_file, previous_assignment_file)
        secret_santa.assign_secret_santas()
        secret_santa.save_assignments(output_file)
        print(f"Secret Santa assignments saved to {output_file}.")
    except Exception as e:
        print(f"An error occurred: {e}")
