import mlflow
import numpy as np
def classify_customer(train):
    train_df = train.drop(columns=['id'])

    train_df['Age_group'] = ''
    i = 0
    cnt = 1
    while(i<100):
        age_index = train_df[(train_df['Age'] >= i) & (train_df['Age'] < i+25)].index
        train_df.loc[age_index,'Age_group'] = cnt
        i+=25
        cnt+=1

    train_df = train_df.drop(columns=['Age','Gender','Region_Code'])

    vehicle_damage_index = train_df[train_df['Vehicle_Damage'] == 'Yes'].index
    vehicle_not_damage_index = train_df[train_df['Vehicle_Damage'] == 'No'].index
    train_df.loc[vehicle_damage_index,'Vehicle_Damage'] = 1
    train_df.loc[vehicle_not_damage_index,'Vehicle_Damage'] = 0

    vehicle_age_0_index = train_df[train_df['Vehicle_Age'] == '< 1 Year'].index
    vehicle_age_1_index = train_df[train_df['Vehicle_Age'] == '1-2 Year'].index
    vehicle_age_2_index = train_df[train_df['Vehicle_Age'] == '> 2 Years'].index
    train_df.loc[vehicle_age_0_index,'Vehicle_Age'] = 0
    train_df.loc[vehicle_age_1_index,'Vehicle_Age'] = 1
    train_df.loc[vehicle_age_2_index,'Vehicle_Age'] = 2

    train_df[['Vehicle_Age','Vehicle_Damage','Age_group']] = train_df[['Vehicle_Age','Vehicle_Damage','Age_group']].astype('int64')

    train_df.columns = [col.replace('[', '_').replace(']', '_').replace('<', '_').replace('>', '_') for col in train_df.columns]

    model_uri = "models:/DEV_Model@challenger"
    xgb_model = mlflow.xgboost.load_model(model_uri)

    prediction = xgb_model.predict_proba(train_df)
    prediction = np.round(prediction[:,1]*100,2)
    print(prediction)
    if prediction >= 70:
        return "Will take the insurance"
    elif prediction <= 30:
        return "Will not take the insurance"
    else:
        return "Undecided (probability is between 0.3 and 0.7)"
