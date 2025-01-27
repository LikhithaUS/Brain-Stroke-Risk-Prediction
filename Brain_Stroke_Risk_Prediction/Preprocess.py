import numpy as np # linear algebra
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats
import plotly.express as pt
import warnings
from sklearn import preprocessing
warnings.filterwarnings('ignore')
def process():
    
    df = pd.read_csv("./Dataset/healthcare-dataset-stroke-data.csv")
    data = pd.read_csv("./Dataset/healthcare-dataset-stroke-data.csv")
    print(df.head())
    print('\njust browsing how the data looks, we can see some nan in BMI\n')
    print(df.info)
    print('#1 generating descriptive stats\n')

    dfA = pd.DataFrame(data)
    stats = dfA['bmi'].describe()
    print(stats)
    print('Now for everyone!')
    dfA = pd.DataFrame(data)
    statsB = dfA.describe(include='all')
    print(statsB)
    print('\n#2 a barplot for smokers who had a stroke\n')

    genders = dfA['gender']
    strokes = dfA['stroke']

    fig = plt.figure(figsize = (10,15))
    plt.bar(genders, strokes , color ='maroon', width = 0.4 )

    plt.xlabel("Gender specific")
    plt.ylabel("Stroke risk")
    plt.show()
    print('\n#3 code for the Distribution plot\n')

    sns.displot(x=data['age'],y=data['stroke'])

    print('im not sure if I did it right as the results to show the darker colors are more indicative of stroke risk which corrolate above')
    print('to the 1.0 stroke rate\n')
    print('\n#4 the code for the Violin plot attempt\n')

    data = pd.read_csv("./Dataset/healthcare-dataset-stroke-data.csv")
    dfA = pd.DataFrame(data)
    data = dfA.head()
    fig = pt.violin(data,x=dfA['stroke'],y = dfA['age'], points='all')
    fig.show()
    print('\n#5 Now looking at the data for both, it appears that the male plot is one giant risk factor while for females it is more prevlant once  ')
    print('the 80 year mark is reached. This would be imbalanced for the men and balanced for the females, perhaps some more criteria is needed for males.')
    print('\n#6 Heatmap time!\n')
    plt.figure(figsize=(16,10))
    sns.heatmap(data.corr(method='pearson'), annot=True)
    print('\nHypertension seems to be a leading indicator for stroke risk with BMI paired right with it\n')
    print('\n#7 Finding the outliers threshhold\n')


    #calculating outliers for Average glucose
    meanAvgGlu = dfA['avg_glucose_level'].mean()
    stdAvgGlu = dfA['avg_glucose_level'].std()

    outliersThreshA = meanAvgGlu + 3 * stdAvgGlu
    outliersA = dfA.loc[dfA['avg_glucose_level'] > outliersThreshA]



    #calculating outliers for BMI
    meanBmi = dfA['bmi'].mean()
    stdBmi = dfA['bmi'].std()

    outliersThreshB = meanBmi +3 * stdBmi
    outliersB = dfA.loc[dfA['bmi'] > outliersThreshB]

    dfB = dfA.loc[dfA['avg_glucose_level'] <= outliersThreshA]
    dfB = dfA.loc[dfA['bmi'] <= outliersThreshA]

    print('\nBMI Outliers: ',outliersThreshB ,'\nGlucose Outliers: ',outliersThreshA ,'\n')

    print('\n#8 Now attempting to change the null values to averaged out values\n')
    dfA['bmi'].fillna(value=meanBmi, inplace=True)
    stdBmiA = dfA['bmi'].std()
    outlierThreshMod = meanBmi +3 * stdBmi
    outliersMod = dfA.loc[dfA['bmi'] > outlierThreshMod]
    dfC = dfA.loc[df['bmi'] <= outlierThreshMod]

    nulledOut =dfC.isnull().sum()
    print(nulledOut,'\n')

    stats = dfA['bmi'].describe()
    print(stats)
    print('\n#9 this is converting variables to object data types\n')
    labelEncoder = preprocessing.LabelEncoder()
    print('\nthere are 5 data types that are object, they are: gender, ever married, work type, residence type, smoking status\n')

    print('\nGender ',df['gender'].unique())
    print('\nEver Married ',df['ever_married'].unique())
    print('\nWork Type',df['work_type'].unique())
    print('\nResidence ',df['Residence_type'].unique())
    print('\nSmoking status ',df['smoking_status'].unique())

    print('\n\nWe will now show the objects encoded into integers\n')
    dfA['gender'] = labelEncoder.fit_transform(dfA['gender'])
    print('\nGender ',dfA['gender'].unique())

    dfA['ever_married'] = labelEncoder.fit_transform(dfA['ever_married'])
    print('\nEver Married ',dfA['ever_married'].unique())

    dfA['work_type'] = labelEncoder.fit_transform(dfA['work_type'])
    print('\nWork Type',dfA['work_type'].unique())


    dfA['Residence_type'] = labelEncoder.fit_transform(dfA['Residence_type'])
    print('\nResidence ',dfA['Residence_type'].unique())


    dfA['smoking_status'] = labelEncoder.fit_transform(dfA['smoking_status'])
    print('\nSmoking status ',dfA['smoking_status'].unique())
    dfA.to_csv("Preprocessed.csv")
