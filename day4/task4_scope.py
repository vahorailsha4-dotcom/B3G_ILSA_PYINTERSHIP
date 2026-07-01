def task_studnet():
    status="pending"
    def complete():
        nonlocal status
        status="completed"
    complete()
    print("Final Status:",status)
    task_status()
    