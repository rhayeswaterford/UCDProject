# Richard Hayes's Project for UCD PA Data Analytics Course October 2021
#
# The project investigates higher education student enrolment patterns in Ireland for 2018-19. The project uses data supplied by the Higher Education Authority.
# the project is particularly interested in enrolment patterns within and outside the SE of Ireland and, specifically, in the pattern of enrolment of students
# with a domiciliary origin of the SE of Ireland who study outside the SE of Ireland. The project seeks to parse the data to identify the course disciplinary areas,
# institution type, and institution that enrol students from the SE but are outside the SE. The project will in this way offer an analysis of the "brain drain" of
# students from the SE of Ireland.
#
# Section 1 Import relevant packages: equip the engine!!!
import pandas as pd

# Section 2 Import the data
studentdata = pd.read_csv('HEA_Student_Enrolment_Data_Domicilary_Origin_2018-19.csv')

# Section 3 Create the DataFrame
df = pd.DataFrame(studentdata)

check1 = df.shape
check2 = df.info()
check3 = df.describe()
check4 = df.values
check5 = df.columns
check6 = df.index

# print(check1)
# print(check2)
# print(check3)
print(check4)
print(check5)
print(check6)

# Section 3a Clean up the DataFrame


# Section 4 Analyse the Data

# 4a Enrolment by Institution Type
# 4b Enrolment by Institution
# 4c Enrolment by County
# 4d Enrolment by County by Institution Type
# 4e Enrolment by County by Institution
# 4f Enrolment by SE Counties
# 4g Enrolment by SE Counties by Institution
# 4h Enrolment by SE Counties by INstitution by DIscipline
# 4i Brain Drain
