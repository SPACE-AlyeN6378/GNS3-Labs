import os


# TITLE
title = ""
while not title:
    title = input("Lab Title: ").strip()
print()
md_lines = [f"# {title}\n"]

# SCENARIO
scenario = input("Scenario: ").strip()
if scenario:
    md_lines.append(f"## Scenario\n")
    md_lines.append(scenario + "\n\n")
print()

# TOPOLOGY
md_lines.append(f"### Topology:\n")
topology = ""
while not topology:
    topology = input("Topology filename: ").strip()

md_lines.append(f"![Topology](./{topology})\n\n")

# TASKS
print("Enter the tasks below: ")
md_lines.append("## Tasks\n")
bullet_pts = input("- ")
while bullet_pts != "":
    if bullet_pts[0] == '\t':
        bullet_pts = bullet_pts.replace('\t', '')
        bullet_pts = "\t* " + bullet_pts
    else:
        bullet_pts = "- " + bullet_pts

    md_lines.append(bullet_pts)
    bullet_pts = input("- ")

md_lines.append("\n\n")

# SAVE DESTINATION
save_destination = ""
confirmed = False
while not (confirmed or save_destination.strip()):
    try:
        save_destination = input("Where to save: ")
        os.chdir("..")
        os.chdir(save_destination)
        confirmed = True
    except:
        print("Invalid destination")

with open("readme.md", "w") as file:
    file.write("\n".join(md_lines))
    
