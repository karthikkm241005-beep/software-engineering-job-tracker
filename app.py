import json
import os

FILE_NAME = "jobs.json"

def load_jobs():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_jobs(jobs):
    with open(FILE_NAME, "w") as file:
        json.dump(jobs, file, indent=4)

def add_job():
    company = input("Company Name: ")
    title = input("Job Title: ")
    location = input("Location: ")
    
    job = {
        "company": company,
        "title": title,
        "location": location,
        "status": "Applied"
    }

    jobs = load_jobs()
    jobs.append(job)
    save_jobs(jobs)
    print("Job added successfully!")

def view_jobs():
    jobs = load_jobs()
    if not jobs:
        print("No jobs found.")
        return
    
    for i, job in enumerate(jobs, start=1):
        print(f"{i}. {job['company']} - {job['title']} ({job['location']}) [{job['status']}]")

def main():
    while True:
        print("\n1. Add Job\n2. View Jobs\n3. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_job()
        elif choice == "2":
            view_jobs()
        elif choice == "3":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
