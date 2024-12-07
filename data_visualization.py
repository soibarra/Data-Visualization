import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.DataFrame({
    'Diagnosis_Code': ['A01', 'B02', 'A01', 'C03', 'B02'],
    'Provider_ID': [101, 102, 101, 103, 102],
    'Treatment_Cost': [200, 400, 150, 0, 450]
})

# Visualization 1: Patient Count by Diagnosis Code
patient_count = data['Diagnosis_Code'].value_counts()
plt.figure(figsize=(8, 6))
patient_count.plot(kind='bar', color='skyblue')
plt.title('Patient Count by Diagnosis Code', fontsize=14)
plt.xlabel('Diagnosis Code', fontsize=12)
plt.ylabel('Patient Count', fontsize=12)
plt.xticks(rotation=0)
plt.savefig('patient_count_by_diagnosis.png')  # Save the figure
plt.close()  # Close the plot to avoid GUI issues

# Visualization 2: Total Treatment Costs by Provider
costs_by_provider = data.groupby('Provider_ID')['Treatment_Cost'].sum()
plt.figure(figsize=(8, 6))
costs_by_provider.plot(kind='bar', color='lightgreen')
plt.title('Total Treatment Costs by Provider', fontsize=14)
plt.xlabel('Provider ID', fontsize=12)
plt.ylabel('Total Treatment Cost ($)', fontsize=12)
plt.xticks(rotation=0)
plt.savefig('treatment_costs_by_provider.png')  # Save the figure
plt.close()  # Close the plot to avoid GUI issues

print("Visualizations saved as PNG files.")

