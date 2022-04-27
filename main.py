import pandas as pd
import matplotlib.pyplot as plt

pd.set_option('display.max_columns', 30)

general = pd.read_csv('test/general.csv')
prenatal = pd.read_csv('test/prenatal.csv')
sports = pd.read_csv('test/sports.csv')

general.columns = [',', 'hospital', 'gender', 'age', 'height', 'weight', 'bmi', 'diagnosis',
                   'blood_test', 'ecg', 'ultrasound', 'mri', 'xray', 'children', 'months']
prenatal.columns = [',', 'hospital', 'gender', 'age', 'height', 'weight', 'bmi', 'diagnosis',
                    'blood_test', 'ecg', 'ultrasound', 'mri', 'xray', 'children', 'months']
sports.columns = [',', 'hospital', 'gender', 'age', 'height', 'weight', 'bmi', 'diagnosis',
                  'blood_test', 'ecg', 'ultrasound', 'mri', 'xray', 'children', 'months']

all_data = pd.concat([general, prenatal, sports], ignore_index=True)
all_data.drop(columns=[','], inplace=True)
all_data.dropna(axis=0, thresh=1, inplace=True)
all_data['gender'].replace(['female', 'male', 'man', 'woman'], ['f', 'm', 'm', 'f'], inplace=True)
all_data['gender'].fillna('f', inplace=True)
all_data[['bmi', 'diagnosis', 'blood_test', 'ecg', 'ultrasound', 'mri', 'xray', 'children', 'months']] = \
    all_data[['bmi', 'diagnosis', 'blood_test', 'ecg', 'ultrasound', 'mri', 'xray', 'children', 'months']] \
        .fillna(value=0)

# print(all_data.shape)
# print(all_data.sample(n=20, random_state=30))
# print(all_data)
"""
q1 = all_data['hospital'].value_counts().index.tolist()[0]

q2 = all_data.loc[all_data['hospital'] == 'general']['diagnosis'].value_counts(normalize=True)['stomach'].round(3)

q3 = all_data.loc[all_data['hospital'] == 'sports']['diagnosis'].value_counts(normalize=True)['dislocation'].round(3)

q4 = all_data.loc[all_data['hospital'] == 'general']['age'].median()
q4 = q4 - all_data.loc[all_data['hospital'] == 'sports']['age'].median()

q5 = all_data.pivot_table(index='hospital', columns='blood_test', values='age', aggfunc='count', sort=True)
q5_1 = q5['t'].sort_values(ascending=False).index.tolist()[0]
q5_2 = max(q5.iloc[:, 2])
"""

# age histogram starts here
g_age = all_data.loc[all_data['hospital'] == 'general']['age']
p_age = all_data.loc[all_data['hospital'] == 'prenatal']['age']
s_age = all_data.loc[all_data['hospital'] == 'sports']['age']
age_bins = [0, 15, 35, 55, 70, 80]
age_lab = ["General", "Prenatal", "Sports"]
plt.hist([g_age, p_age, s_age], bins=age_bins, label=age_lab)
plt.title("Age distribution among all Hospitals")
plt.ylabel("Number of people")
plt.xlabel("Age in Yrs")
plt.legend()
plt.show()

# diagnosis pie chart starts here
pie_diag = all_data['diagnosis'].value_counts()
diag_lab = [x for x in all_data['diagnosis'].value_counts().index.tolist()]
plt.figure(figsize=(9, 9))
plt.pie(pie_diag)
plt.title('Diagnosis among all hospitals', fontsize=14)
plt.legend(diag_lab)
plt.show()

# height violin plot starts here
g_height = all_data.loc[all_data['hospital'] == 'general']['height']
p_height = all_data.loc[all_data['hospital'] == 'prenatal']['height']
s_height = all_data.loc[all_data['hospital'] == 'sports']['height']
height_list = [g_height, p_height, s_height]
fig, axes = plt.subplots()
plt.violinplot(height_list)
axes.set_xticks((1, 2, 3))
axes.set_xticklabels(("General", "Prenatal", "Sports"))
axes.set_ylabel("Height in cm or ft")
axes.set_title('Height Violin plot')
sal = plt.violinplot(height_list, showextrema=True, showmeans=True, showmedians=True, quantiles=[[0.25, 0.75, 0.9], [0.25, 0.75, 0.9], [0.25, 0.75, 0.9]])
sal['cmeans'].set_color('m')
sal['cmedians'].set_color('g')
sal['cquantiles'].set_color('r')
plt.show()

q1 = '15-35'
q2 = 'pregnancy'
q3 = 'This is because two of the hospitals produce height measurements in [m], whereas the third does it in [ft].'

print("""The answer to the 1st question: {}
The answer to the 2nd question: {}
The answer to the 3rd question: {}""".format(q1, q2, q3))
