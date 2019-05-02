import requests

def get_status_code(url):
    try:
        r = requests.get(url)
        print ("Processing " + url)

        if len(r.history) > 0:
            chain = ""
            code = r.history[0].status_code
            final_url = r.url
            for resp in r.history:
                chain += resp.url + " | "
            return str(code) + '\t' + str(len(r.history)) + '\t' + chain + '\t' + final_url + '\t'
        else:
            return str(r.status_code) + '\t\t\t\t'
    except requests.ConnectionError:
        print("Error: failed to connect.")
        return '0\t\t\t\t'


input_file = 'PDF.txt'
output_file = 'output.txt'

with open(output_file, 'w') as o_file:
    o_file.write('URL\tStatus\tNumber of redirects\tRedirect Chain\tFinal URL\t\n')
    f = open(input_file, "r")
    lines = f.read().splitlines()
    for line in lines:
        code = get_status_code(line)
        o_file.write(line + "\t" + str(code) + "\t\n")
    f.close()