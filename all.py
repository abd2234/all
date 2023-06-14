import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load the diabetes dataset
diabetes = pd.read_csv('diabetes cleaned8.csv')



# Section 1: Picture
st.title("Diabetes")
st.header("Section 1: Picture")


# Section 2: Introduction
st.header("Section 2: Introduction")
st.write("Diabetes is a chronic metabolic disorder characterized by high blood sugar levels over a prolonged period. It occurs when the body either does not produce enough insulin or does not effectively use the insulin it produces. Insulin is a hormone that regulates blood sugar levels and allows glucose to enter cells to be used as energy.")

# Section 3: Visualization
st.header("Section 3: Visualization")

# Visualize the distribution of age
st.subheader("Age Distribution")
fig, ax = plt.subplots()
sns.histplot(diabetes['Age'], kde=True, ax=ax)
st.pyplot(fig)

# Visualize the distribution of BMI
st.subheader("BMI Distribution")
fig, ax = plt.subplots()
sns.histplot(diabetes['BMI'], kde=True, ax=ax)
st.pyplot(fig)

# Visualize the distribution of number of times pregnant
st.subheader("Number of Times Pregnant Distribution")
fig, ax = plt.subplots()
sns.histplot(diabetes['Number of times pregnant'], kde=True, ax=ax)
st.pyplot(fig)

# Section 3: Visualization
st.header("Section 3: Visualization")

# Create a countplot to visualize the relationship between "Smoking" and "Diabetic"
st.subheader("Relationship between Smoking and Diabetic")
sns.countplot(x='Smoking', hue='Diabetic', data=diabetes)

# Set the plot title and labels
plt.title('Relationship between Smoking and Diabetic')
plt.xlabel('Smoking')
plt.ylabel('Count')

# Display the plot
st.pyplot()
# Section 3: Visualization
st.header("Section 3: Visualization")

# Calculate the count of each category in the "Smoking" column
smoking_counts = diabetes['Smoking'].value_counts()

# Create a pie chart to visualize the distribution
st.subheader("Distribution of Smoking Status")
fig, ax = plt.subplots()
ax.pie(smoking_counts, labels=smoking_counts.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.title("Distribution of Smoking Status")
st.pyplot(fig)

# Create a countplot to visualize the relationship between "Smoking" and "Diabetic"
st.subheader("Relationship between Smoking and Diabetic")
sns.countplot(x='Smoking', hue='Diabetic', data=diabetes)

# Set the plot title and labels
plt.title('Relationship between Smoking and Diabetic')
plt.xlabel('Smoking')
plt.ylabel('Count')

# Display the plot
st.pyplot()

# Section 3: Visualization
st.header("Section 3: Visualization")

# Calculate the count of each category in the "Alcohol" column
alcohol_counts = diabetes['Alcohol'].value_counts()

# Create a pie chart to visualize the distribution
st.subheader("Distribution of Alcohol Consumption")
fig, ax = plt.subplots()
ax.pie(alcohol_counts, labels=alcohol_counts.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.title("Distribution of Alcohol Consumption")
st.pyplot(fig)

# Create a countplot to visualize the relationship between "Alcohol" and "Diabetic"
st.subheader("Relationship between Alcohol Consumption and Diabetic")
sns.countplot(x='Alcohol', hue='Diabetic', data=diabetes)

# Set the plot title and labels
plt.title('Relationship between Alcohol Consumption and Diabetic')
plt.xlabel('Alcohol')
plt.ylabel('Count')

# Display the plot
st.pyplot()

# Calculate the count of each category in the "stress" column
stress_counts = diabetes['Stress'].value_counts()

# Create a pie chart to visualize the distribution
st.subheader("Distribution of Stress")
fig, ax = plt.subplots()
ax.pie(stress_counts, labels=stress_counts.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.title("Distribution of Stress")
st.pyplot(fig)

# Create a countplot to visualize the relationship between "stress" and "Diabetic"
st.subheader("Relationship between Stress and Diabetic")
sns.countplot(x='Stress', hue='Diabetic', data=diabetes,
              order=['Not at all', 'Sometimes', 'Often', 'Very often', 'Always'])

# Set the plot title and labels
plt.title('Relationship between Stress and Diabetic')
plt.xlabel('Stress')
plt.ylabel('Count')

# Display the plot
st.pyplot()

# Section 3: Visualization
st.header("Section 3: Visualization")

# Create a countplot to visualize the relationship between "Gender" and "Diabetic"
st.subheader("Relationship between Gender and Diabetic")
sns.countplot(x='Gender', hue='Diabetic', data=diabetes)

# Set the plot title and labels
plt.title('Relationship between Gender and Diabetic')
plt.xlabel('Gender')
plt.ylabel('Count')

# Display the plot
st.pyplot()
import streamlit as st

# Section 3: Visualization
st.header("Section 3: Visualization")

# Create a checkbox for filtering diabetic cases
diabetic_filter1 = st.checkbox("Show Diabetic Cases")

# Filter the dataset based on the checkbox selection
if diabetic_filter1:
    filtered_data = diabetes[diabetes['Diabetic'] == 1]
    title = 'Relationship between Family Diabetes and Diabetic (Diabetic Cases)'
else:
    filtered_data = diabetes
    title = 'Relationship between Family Diabetes and Diabetic (All Cases)'

# Create a countplot to visualize the relationship between "Family_Diabetes" and "Diabetic"
st.subheader(title)
sns.countplot(x='Family_Diabetes', hue='Diabetic', data=filtered_data)

# Set the plot title and labels
plt.title(title)
plt.xlabel('Family Diabetes')
plt.ylabel('Count')

# Display the plot
st.pyplot()

# Section 3: Visualization
st.header("Section 3: Visualization")

# Create a checkbox for filtering diabetic cases
diabetic_filter2 = st.checkbox("Show Diabetic Cases", key="diabetic_filter")

# Filter the dataset based on the checkbox selection
if diabetic_filter2:
    filtered_data = diabetes[diabetes['Diabetic'] == 1]
    title = 'Relationship between Regular Medicine and Diabetic (Diabetic Cases)'
else:
    filtered_data = diabetes
    title = 'Relationship between Regular Medicine and Diabetic (All Cases)'

# Create a countplot to visualize the relationship between "RegularMedicine" and "Diabetic"
st.subheader(title)
fig, ax = plt.subplots()
sns.countplot(x='RegularMedicine', hue='Diabetic', data=filtered_data)

# Set the plot title and labels
plt.title(title)
plt.xlabel('Regular Medicine')
plt.ylabel('Count')

# Update the legend labels
legend_labels = ['0: Does Not Take Medicine', '1: Takes Medicine']
handles, _ = ax.get_legend_handles_labels()
ax.legend(handles, legend_labels, title='Diabetic')

# Display the plot
st.pyplot(fig)




# Section 3: Visualization
st.header("Section 3: Visualization")

# Create a countplot to visualize the relationship between "JunkFood" and "Diabetic"
st.subheader("Relationship between Junk Food and Diabetic")
sns.countplot(x='JunkFood', hue='Diabetic', data=diabetes)

# Set the plot title and labels
plt.title('Relationship between Junk Food and Diabetic')
plt.xlabel('Junk Food')
plt.ylabel('Count')

# Add legend
plt.legend(title='Diabetic')

# Display the plot
st.pyplot()
# Section 3: Visualization
st.header("Section 3: Visualization")

# Create a countplot to visualize the relationship between "Blood Pressure level" and "Diabetic"
st.subheader("Relationship between Blood Pressure Level and Diabetic")
sns.countplot(x='BloodPressure level', hue='Diabetic', data=diabetes)

# Set the plot title and labels
plt.title('Relationship between Blood Pressure Level and Diabetic')
plt.xlabel('Blood Pressure Level')
plt.ylabel('Count')

# Add legend
plt.legend(title='Diabetic')

# Display the plot
st.pyplot()
st.header("Section 3: Visualization")

# Visualize the relationship between BMI and Diabetic using a box plot
st.subheader("BMI vs Diabetic (Box Plot)")
fig, ax = plt.subplots()
sns.boxplot(x='Diabetic', y='BMI', data=diabetes)
plt.xlabel("Diabetic")
plt.ylabel("BMI")
st.pyplot(fig)

# Visualize the relationship between BMI and Diabetic using a violin plot
st.subheader("BMI vs Diabetic (Violin Plot)")
fig, ax = plt.subplots()
sns.violinplot(x='Diabetic', y='BMI', data=diabetes)
plt.xlabel("Diabetic")
plt.ylabel("BMI")
st.pyplot(fig)
# Section 3: Visualization

# Section 3: Visualization
st.header("Section 3: Visualization")

# Create a countplot to visualize the relationship between "PhysicallyActive" and "Diabetic"
st.subheader("Relationship between Physically Active and Diabetic")
sns.countplot(x='PhysicallyActive', hue='Diabetic', data=diabetes)

# Set the plot title and labels
plt.title('Relationship between Physically Active and Diabetic')
plt.xlabel('Physically Active')
plt.ylabel('Count')

# Add legend
plt.legend(title='Diabetic')

# Display the plot
st.pyplot()
# Violin plot to visualize the relationship between "Sleeping hours" and "Diabetic"
st.subheader("Relationship between Sleeping Hours and Diabetic (Violin Plot)")
sns.violinplot(x='Diabetic', y='Sleeping hours', data=diabetes)

# Set the plot title and labels
plt.title('Relationship between Sleeping Hours and Diabetic')
plt.xlabel('Diabetic')
plt.ylabel('Sleeping Hours')

# Display the plot
st.pyplot()
# Section 3: Visualization
st.header("Section 3: Visualization")

# Calculate the count of each category in the "Gender" column
gender_counts = diabetes['Gender'].value_counts()

# Create a pie chart to visualize the distribution
st.subheader("Distribution of Gender")
fig, ax = plt.subplots()
ax.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
plt.title("Distribution of Gender")
st.pyplot(fig)
# Section 3: Visualization
st.header("Section 3: Visualization")

# Get user input for BMI value
bmi_input = st.number_input("Enter BMI value", min_value=0.0)

# Filter the data based on the input BMI value
filtered_data = diabetes[diabetes['BMI'] == bmi_input]

# Display the filtered data and its relationship with being diabetic
st.subheader("Relationship between BMI and Diabetic (Filtered Data)")
st.dataframe(filtered_data)

# Visualize the relationship between BMI and Diabetic using a box plot
st.subheader("BMI vs Diabetic (Box Plot)")
fig, ax = plt.subplots()
sns.boxplot(x='Diabetic', y='BMI', data=diabetes)
plt.xlabel("Diabetic")
plt.ylabel("BMI")

# Highlight the input BMI value on the plot
if bmi_input in diabetes['BMI'].values:
    ax.scatter(x=diabetes['Diabetic'], y=[bmi_input] * len(diabetes), color='red', label='Input BMI')

plt.legend()
st.pyplot(fig)

# Visualize the relationship between BMI and Diabetic using a violin plot
st.subheader("BMI vs Diabetic (Violin Plot)")
fig, ax = plt.subplots()
sns.violinplot(x='Diabetic', y='BMI', data=diabetes)
plt.xlabel("Diabetic")
plt.ylabel("BMI")

# Highlight the input BMI value on the plot
if bmi_input in diabetes['BMI'].values:
    ax.scatter(x=diabetes['Diabetic'], y=[bmi_input] * len(diabetes), color='red', label='Input BMI')

plt.legend()
st.pyplot(fig)
# Create a button for gender selection
gender = st.radio("Select Gender", ('All', 'Male', 'Female'))

# Filter the dataset based on gender selection
if gender == 'All':
    filtered_data = diabetes
elif gender == 'Male':
    filtered_data = diabetes[diabetes['Gender'] == 'Male']
else:
    filtered_data = diabetes[diabetes['Gender'] == 'Female']

# Count the number of diabetic cases in the filtered dataset
diabetic_count = filtered_data[filtered_data['Diabetic'] == 1]['Diabetic'].count()

# Create a pie chart to visualize the distribution
st.subheader(f"Distribution of Gender (Diabetic: {diabetic_count})")
fig, ax = plt.subplots()
ax.pie(filtered_data['Gender'].value_counts(), labels=filtered_data['Gender'].value_counts().index, autopct='%1.1f%%', startangle=90)
ax.axis('equal')
plt.title("Distribution of Gender")

# Display the plot
st.pyplot(fig)
# Section 3: Visualization
st.header("Section 3: Visualization")

# Create a checkbox for filtering diabetic cases
diabetic_filter3 = st.checkbox("Show Diabetic Cases")

# Filter the dataset based on the checkbox selection
if diabetic_filter3:
    filtered_data = diabetes[diabetes['Diabetic'] == 1]
    title = 'Relationship between Gender and Diabetic (Diabetic Cases)'
else:
    filtered_data = diabetes[diabetes['Diabetic'] == 0]
    title = 'Relationship between Gender and Diabetic (Non-Diabetic Cases)'

# Create a countplot to visualize the relationship between "Gender" and "Diabetic"
st.subheader(title)
sns.countplot(x='Gender', data=filtered_data)

# Set the plot title and labels
plt.title(title)
plt.xlabel('Gender')
plt.ylabel('Count')

# Display the plot
st.pyplot()
# Section 3: Visualization
st.header("Section 3: Visualization")

# Create a checkbox for filtering diabetic cases
diabetic_filter4 = st.sidebar.checkbox("Show Diabetic Cases")

# Filter the dataset based on the checkbox selection
if diabetic_filter4:
    filtered_data = diabetes[diabetes['Diabetic'] == 1]
    title = 'Relationship between Age and Diabetic (Diabetic Cases)'
else:
    filtered_data = diabetes
    title = 'Relationship between Age and Diabetic (All Cases)'

# Visualize the distribution of age
st.subheader(title)
fig, ax = plt.subplots()
sns.histplot(filtered_data['Age'], kde=True, ax=ax)
plt.xlabel('Age')
plt.ylabel('Count')

# Display the plot
st.pyplot(fig)










