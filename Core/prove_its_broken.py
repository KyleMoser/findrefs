import contrived

delete_ou_activity_arn = contrived.configure_params("contrived example")

def worker():
    print("Find All References does not work if you right click the 'configure_params' in contrived.py; but it does work if you do it in this file.")

worker()