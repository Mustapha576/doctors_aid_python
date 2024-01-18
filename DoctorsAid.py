# reading the input file function
def read():
    return open("doctors_aid_inputs.txt", "r")

outputs = [] # Creating an outputs list to take all the outputs in list.
patients = [] # Creating patients list with their diagnosis accuracy,disease name etc.
patients_names = [] # Creating patients list with only their names in it

# A creating new patient function
def create():
    if line.startswith("create"): # if input line starts with create then it will append patients list and patients names list also give an output.
        row = line.split(", ")
        row[0] = row[0].lstrip("create ").rstrip()
        outputs.append(f"Patient {row[0]} is recorded.")
        row[5] = row[5].rstrip()
        patients.append(row)
        patients_names.append(row[0])
    else: # if not;
        row = line.split(", ")
        row[0] = row[0].lstrip("create ")
        outputs.append(f"Patient {row[0]} cannot be recorded due to duplication.") # it gives an output like this

# Delete an existing patient
def remove():
    row1 = line.lstrip("remove ").rstrip() # it lets only the name
    for i in patients: # it checks all patients list
        if row1 in i[0]: # if name matches in patients list than removes the name from patients and patient_names list
            outputs.append(f"Patient {row1} is removed.")
            patients.remove(i)
            patients_names.remove(row1)
            return patients
        else: # if not then passes
            pass
    if row1 not in patients_names: # if the name dont matches with any of patients_names list than output should be:
        outputs.append(f"Patient {row1} cannot be removed due to absence.")


# a listing function
def listing():
    # I created a new list called listeleme and append all my patients top to bottom and then put it into my outputs list
    eleman = ""
    listeleme = []
    listeleme.append("Patient " + "Diagnosis" + "   " + "Disease" + "         " + "Disease" + "     " + "Treatment" + "       " + "Treatment")
    listeleme.append("Name" + "    " + "Accuracy" + "    " + "Name" + "            " + "Incidence" + "   " + "Name" + "            " + "Risk")
    listeleme.append("-" * 73)
    for i in patients:
        if len(i[0]) < 8:
            eleman += (i[0] + " " * (8 - len(i[0])))
        if len(i[1]) < 12:
            x = str(float(i[1]) * float(100))
            if len(x) < 5:
                x = x + "0"
            eleman += x + "%" + " " * (11 - len(x))
        if len(i[2]) < 16:
            eleman += i[2] + " " * (16 - len(i[2]))
        if len(i[3]) < 12:
            eleman += i[3] + " " * (12 - len(i[3]))
        if len(i[4]) <= 16:
            eleman += i[4] + " " * (16 - len(i[4]))
        if len(i[5]) <= 4:
            eleman += str(int(float(i[5]) * 100)) + "%" + " " * (4 - len(i[5]))
        listeleme.append(eleman)
        eleman = ""
    for j in listeleme:
        outputs.append(j)


# patient's probability of having the disease function
def probability():
    row2 = line.lstrip("probability ").rstrip()
    for k in patients: # If the name matches with anyone of my patients list, it gives an output for probability like this:
        if row2 == k[0]:
            b = k[3].split("/")
            a = str(float(k[1]) * float(100))
            if len(a) < 5:
                a = a + "0"
            nominator, denominator = b
            c = (float(denominator) - float(nominator)) * ((100 - float(a)) / float(100))
            d = float(100) * (float(nominator) / (float(nominator) + float(c)))
            t = round(d, 2)
            e = k[2].rstrip()
            outputs.append(f"Patient {row2} has a probability of {t}% of having {e}.")

        else: # If not it passes
            pass
    if row2 not in patients_names: # If there is no match in patients_names list then it gives an output like this:
        outputs.append(f"Probability for {row2} cannot be calculated due to absence.")

# recommendation function
def recommendation():
    row3 = line.lstrip("recommendation ").rstrip()
    for l in patients:
        if row3 == l[0]: # If the name matches with anyone of my patients list, it gives an output for recommendation like this:
            b = l[3].split("/")
            a = str(float(l[1]) * float(100))
            if len(a) < 5:
                a = a + "0"
            nominator, denominator = b
            c = (float(denominator) - float(nominator)) * ((100 - float(a)) / float(100))
            d = float(100) * (float(nominator) / (float(nominator) + float(c)))
            t = round(d, 2)
            if (float(l[5]) * 100) > float(t):
                outputs.append(f"System suggests {l[0]} NOT to have the treatment.")
                break
            else:
                outputs.append(f"System suggest {l[0]} to have the treatment.")
                break
        else: # If not it passes
            pass
    if row3 not in patients_names: #  If there is no match in patients_names list then it gives an output like this:
        outputs.append(f"Recommendation for {row3} cannot be calculated due to absence.")

def output(): # It opens a new txt file and sets up to print all outputs
    outfile = open("doctors_aid_outputs.txt", "w")
    for line in outputs:
        outfile.write(line + "\n")

def main(): # When we call this function it reads all the inputs txt and analyses it and print all the outputs to txt file
    with read() as file:
        global line
        for line in file:
            if line.startswith("create"):
                create()
            elif line.startswith("remove"):
                remove()
            elif line.startswith("list"):
                listing()
            elif line.startswith("probability"):
                probability()
            elif line.startswith("recommendation"):
                recommendation()
    output()

main()

# Mustafa Anakök 2210356046
