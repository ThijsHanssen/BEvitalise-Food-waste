#%% Adjusting to meet quotas for Flanders dataset

Deletetions_quota = []

""" For Women 18-24 """

while len(FL[(FL['Gender'] == 0) & (FL['Age'] == '18-24')]) > 37:
    if len(FL[FL['Income per month'] == '€4001 – €5000']) > 120:
        index_to_delete = FL[(FL['Gender'] == 0) & (FL['Age'] == '18-24')& (FL['Income per month'] != '> €5000')].sample().index[0]
        Deletetions_quota.append(FL.loc[index_to_delete, 'ID'])
        FL.drop(index_to_delete, inplace=True)
    else:
        index_to_delete = FL[(FL['Gender'] == 0) & (FL['Age'] == '18-24')& (FL['Income per month'] != '> €5000') & (FL['Income per month'] != '€4001 – €5000')].sample().index[0]
        Deletetions_quota.append(FL.loc[index_to_delete, 'ID'])
        FL.drop(index_to_delete, inplace=True)
FL.reset_index(drop=True, inplace=True)

""" For Women 25-34 """

while len(FL[(FL['Gender'] == 0) & (FL['Age'] == '25-34')]) > 47:
    if len(FL[FL['Income per month'] == '€4001 – €5000']) > 120:
        index_to_delete = FL[(FL['Gender'] == 0) & (FL['Age'] == '25-34')& (FL['Income per month'] != '> €5000')].sample().index[0]
        Deletetions_quota.append(FL.loc[index_to_delete, 'ID'])
        FL.drop(index_to_delete, inplace=True)
    else:
        index_to_delete = FL[(FL['Gender'] == 0) & (FL['Age'] == '25-34')& (FL['Income per month'] != '> €5000') & (FL['Income per month'] != '€4001 – €5000')].sample().index[0]
        Deletetions_quota.append(FL.loc[index_to_delete, 'ID'])
        FL.drop(index_to_delete, inplace=True)
FL.reset_index(drop=True, inplace=True)

""" For Women 35-44 """

while len(FL[(FL['Gender'] == 0) & (FL['Age'] == '35-44')]) > 47:
    if len(FL[FL['Income per month'] == '€4001 – €5000']) > 120:
        index_to_delete = FL[(FL['Gender'] == 0) & (FL['Age'] == '35-44')& (FL['Income per month'] != '> €5000')].sample().index[0]
        Deletetions_quota.append(FL.loc[index_to_delete, 'ID'])
        FL.drop(index_to_delete, inplace=True)
    else:
        index_to_delete = FL[(FL['Gender'] == 0) & (FL['Age'] == '35-44')& (FL['Income per month'] != '> €5000') & (FL['Income per month'] != '€4001 – €5000')].sample().index[0]
        Deletetions_quota.append(FL.loc[index_to_delete, 'ID'])
        FL.drop(index_to_delete, inplace=True)
FL.reset_index(drop=True, inplace=True)

""" For Women 45-54 """

while len(FL[(FL['Gender'] == 0) & (FL['Age'] == '45-54')]) > 48:
    if len(FL[FL['Income per month'] == '€4001 – €5000']) > 120:
        index_to_delete = FL[(FL['Gender'] == 0) & (FL['Age'] == '45-54')& (FL['Income per month'] != '> €5000')].sample().index[0]
        Deletetions_quota.append(FL.loc[index_to_delete, 'ID'])
        FL.drop(index_to_delete, inplace=True)
    else:
        index_to_delete = FL[(FL['Gender'] == 0) & (FL['Age'] == '45-54')& (FL['Income per month'] != '> €5000') & (FL['Income per month'] != '€4001 – €5000')].sample().index[0]
        Deletetions_quota.append(FL.loc[index_to_delete, 'ID'])
        FL.drop(index_to_delete, inplace=True)
FL.reset_index(drop=True, inplace=True)

""" For Women 55-64 """

while len(FL[(FL['Gender'] == 0) & (FL['Age'] == '55-64')]) > 49:
    if len(FL[FL['Income per month'] == '€4001 – €5000']) > 120:
        index_to_delete = FL[(FL['Gender'] == 0) & (FL['Age'] == '55-64')& (FL['Income per month'] != '> €5000')].sample().index[0]
        Deletetions_quota.append(FL.loc[index_to_delete, 'ID'])
        FL.drop(index_to_delete, inplace=True)
    else:
        index_to_delete = FL[(FL['Gender'] == 0) & (FL['Age'] == '55-64')& (FL['Income per month'] != '> €5000') & (FL['Income per month'] != '€4001 – €5000')].sample().index[0]
        Deletetions_quota.append(FL.loc[index_to_delete, 'ID'])
        FL.drop(index_to_delete, inplace=True)
FL.reset_index(drop=True, inplace=True)

""" For Women 65+ """

while len(FL[(FL['Gender'] == 0) & (FL['Age'] == '65+')]) > 79:
    if len(FL[FL['Income per month'] == '€4001 – €5000']) > 120:
        index_to_delete = FL[(FL['Gender'] == 0) & (FL['Age'] == '65+')& (FL['Income per month'] != '> €5000')].sample().index[0]
        Deletetions_quota.append(FL.loc[index_to_delete, 'ID'])
        FL.drop(index_to_delete, inplace=True)
    else:
        index_to_delete = FL[(FL['Gender'] == 0) & (FL['Age'] == '65+')& (FL['Income per month'] != '> €5000') & (FL['Income per month'] != '€4001 – €5000')].sample().index[0]
        Deletetions_quota.append(FL.loc[index_to_delete, 'ID'])
        FL.drop(index_to_delete, inplace=True)
FL.reset_index(drop=True, inplace=True)

""" For Men 18-24 """

while len(FL[(FL['Gender'] == 1) & (FL['Age'] == '18-24')]) > 38:
    if len(FL[FL['Income per month'] == '€4001 – €5000']) > 120:
        index_to_delete = FL[(FL['Gender'] == 1) & (FL['Age'] == '18-24')& (FL['Income per month'] != '> €5000')].sample().index[0]
        Deletetions_quota.append(FL.loc[index_to_delete, 'ID'])
        FL.drop(index_to_delete, inplace=True)
    else:
        index_to_delete = FL[(FL['Gender'] == 1) & (FL['Age'] == '18-24')& (FL['Income per month'] != '> €5000') & (FL['Income per month'] != '€4001 – €5000')].sample().index[0]
        Deletetions_quota.append(FL.loc[index_to_delete, 'ID'])
        FL.drop(index_to_delete, inplace=True)
FL.reset_index(drop=True, inplace=True)

""" For Men 25-34 """

while len(FL[(FL['Gender'] == 1) & (FL['Age'] == '25-34')]) > 47:
    if len(FL[FL['Income per month'] == '€4001 – €5000']) > 120:
        index_to_delete = FL[(FL['Gender'] == 1) & (FL['Age'] == '25-34')& (FL['Income per month'] != '> €5000')].sample().index[0]
        Deletetions_quota.append(FL.loc[index_to_delete, 'ID'])
        FL.drop(index_to_delete, inplace=True)
    else:
        index_to_delete = FL[(FL['Gender'] == 1) & (FL['Age'] == '25-34')& (FL['Income per month'] != '> €5000') & (FL['Income per month'] != '€4001 – €5000')].sample().index[0]
        Deletetions_quota.append(FL.loc[index_to_delete, 'ID'])
        FL.drop(index_to_delete, inplace=True)
FL.reset_index(drop=True, inplace=True)

""" For Men 35-44 """

while len(FL[(FL['Gender'] == 1) & (FL['Age'] == '35-44')]) > 47:
    if len(FL[FL['Income per month'] == '€4001 – €5000']) > 120:
        index_to_delete = FL[(FL['Gender'] == 1) & (FL['Age'] == '35-44')& (FL['Income per month'] != '> €5000')].sample().index[0]
        Deletetions_quota.append(FL.loc[index_to_delete, 'ID'])
        FL.drop(index_to_delete, inplace=True)
    else:
        index_to_delete = FL[(FL['Gender'] == 1) & (FL['Age'] == '35-44')& (FL['Income per month'] != '> €5000') & (FL['Income per month'] != '€4001 – €5000')].sample().index[0]
        Deletetions_quota.append(FL.loc[index_to_delete, 'ID'])
        FL.drop(index_to_delete, inplace=True)
FL.reset_index(drop=True, inplace=True)

""" For Men 45-54 """

while len(FL[(FL['Gender'] == 1) & (FL['Age'] == '45-54')]) > 49:
    if len(FL[FL['Income per month'] == '€4001 – €5000']) > 120:
        index_to_delete = FL[(FL['Gender'] == 1) & (FL['Age'] == '45-54')& (FL['Income per month'] != '> €5000')].sample().index[0]
        Deletetions_quota.append(FL.loc[index_to_delete, 'ID'])
        FL.drop(index_to_delete, inplace=True)
    else:
        index_to_delete = FL[(FL['Gender'] == 1) & (FL['Age'] == '45-54')& (FL['Income per month'] != '> €5000') & (FL['Income per month'] != '€4001 – €5000')].sample().index[0]
        Deletetions_quota.append(FL.loc[index_to_delete, 'ID'])
        FL.drop(index_to_delete, inplace=True)
FL.reset_index(drop=True, inplace=True)

""" For Men 55-64 """

while len(FL[(FL['Gender'] == 1) & (FL['Age'] == '55-64')]) > 49:
    if len(FL[FL['Income per month'] == '€4001 – €5000']) > 120:
        index_to_delete = FL[(FL['Gender'] == 1) & (FL['Age'] == '55-64')& (FL['Income per month'] != '> €5000')].sample().index[0]
        Deletetions_quota.append(FL.loc[index_to_delete, 'ID'])
        FL.drop(index_to_delete, inplace=True)
    else:
        index_to_delete = FL[(FL['Gender'] == 1) & (FL['Age'] == '55-64')& (FL['Income per month'] != '> €5000') & (FL['Income per month'] != '€4001 – €5000')].sample().index[0]
        Deletetions_quota.append(FL.loc[index_to_delete, 'ID'])
        FL.drop(index_to_delete, inplace=True)
FL.reset_index(drop=True, inplace=True)

""" For Men 65+ """

while len(FL[(FL['Gender'] == 1) & (FL['Age'] == '65+')]) > 62:
    if len(FL[FL['Income per month'] == '€4001 – €5000']) > 120:
        index_to_delete = FL[(FL['Gender'] == 1) & (FL['Age'] == '65+')& (FL['Income per month'] != '> €5000')].sample().index[0]
        Deletetions_quota.append(FL.loc[index_to_delete, 'ID'])
        FL.drop(index_to_delete, inplace=True)
    else:
        index_to_delete = FL[(FL['Gender'] == 1) & (FL['Age'] == '65+')& (FL['Income per month'] != '> €5000') & (FL['Income per month'] != '€4001 – €5000')].sample().index[0]
        Deletetions_quota.append(FL.loc[index_to_delete, 'ID'])
        FL.drop(index_to_delete, inplace=True)
FL.reset_index(drop=True, inplace=True)


#%% Adjusting to meet quotas for Wallonia dataset

Deletions_quota_WA = []

""" For Women 18-24 """

while len(WA[(WA['Gender'] == 0) & (WA['Age'] == '18-24')]) > 24:
    if len(WA[WA['Income per month'] == '€4001 – €5000']) > 80:
        index_to_delete = WA[(WA['Gender'] == 0) & (WA['Age'] == '18-24') & (WA['Income per month'] != '> €5000') & (WA['Income per month'] != '€1001 – €2000')].sample().index[0]
        Deletions_quota_WA.append(WA.loc[index_to_delete, 'ID'])
        WA.drop(index_to_delete, inplace=True)
    else:
        index_to_delete = WA[(WA['Gender'] == 0) & (WA['Age'] == '18-24') & (WA['Income per month'] != '> €5000') & (WA['Income per month'] != '€4001 – €5000') & (WA['Income per month'] != '€1001 – €2000')].sample().index[0]
        Deletions_quota_WA.append(WA.loc[index_to_delete, 'ID'])
        WA.drop(index_to_delete, inplace=True)
WA.reset_index(drop=True, inplace=True)

""" For Women 25-34 """

while len(WA[(WA['Gender'] == 0) & (WA['Age'] == '25-34')]) > 31:
    if len(WA[WA['Income per month'] == '€4001 – €5000']) > 80:
        index_to_delete = WA[(WA['Gender'] == 0) & (WA['Age'] == '25-34') & (WA['Income per month'] != '> €5000')& (WA['Income per month'] != '€1001 – €2000')].sample().index[0]
        Deletions_quota_WA.append(WA.loc[index_to_delete, 'ID'])
        WA.drop(index_to_delete, inplace=True)
    else:
        index_to_delete = WA[(WA['Gender'] == 0) & (WA['Age'] == '25-34') & (WA['Income per month'] != '> €5000') & (WA['Income per month'] != '€4001 – €5000')& (WA['Income per month'] != '€1001 – €2000')].sample().index[0]
        Deletions_quota_WA.append(WA.loc[index_to_delete, 'ID'])
        WA.drop(index_to_delete, inplace=True)
WA.reset_index(drop=True, inplace=True)

""" For Women 35-44 """

while len(WA[(WA['Gender'] == 0) & (WA['Age'] == '35-44')]) > 32:
    if len(WA[WA['Income per month'] == '€4001 – €5000']) > 80:
        index_to_delete = WA[(WA['Gender'] == 0) & (WA['Age'] == '35-44') & (WA['Income per month'] != '> €5000')& (WA['Income per month'] != '€1001 – €2000')].sample().index[0]
        Deletions_quota_WA.append(WA.loc[index_to_delete, 'ID'])
        WA.drop(index_to_delete, inplace=True)
    else:
        index_to_delete = WA[(WA['Gender'] == 0) & (WA['Age'] == '35-44') & (WA['Income per month'] != '> €5000') & (WA['Income per month'] != '€4001 – €5000')& (WA['Income per month'] != '€1001 – €2000')].sample().index[0]
        Deletions_quota_WA.append(WA.loc[index_to_delete, 'ID'])
        WA.drop(index_to_delete, inplace=True)
WA.reset_index(drop=True, inplace=True)

""" For Women 45-54 """

while len(WA[(WA['Gender'] == 0) & (WA['Age'] == '45-54')]) > 32:
    if len(WA[WA['Income per month'] == '€4001 – €5000']) > 80:
        index_to_delete = WA[(WA['Gender'] == 0) & (WA['Age'] == '45-54') & (WA['Income per month'] != '> €5000')& (WA['Income per month'] != '€1001 – €2000')].sample().index[0]
        Deletions_quota_WA.append(WA.loc[index_to_delete, 'ID'])
        WA.drop(index_to_delete, inplace=True)
    else:
        index_to_delete = WA[(WA['Gender'] == 0) & (WA['Age'] == '45-54') & (WA['Income per month'] != '> €5000') & (WA['Income per month'] != '€4001 – €5000')& (WA['Income per month'] != '€1001 – €2000')].sample().index[0]
        Deletions_quota_WA.append(WA.loc[index_to_delete, 'ID'])
        WA.drop(index_to_delete, inplace=True)
WA.reset_index(drop=True, inplace=True)

""" For Women 55-64 """

while len(WA[(WA['Gender'] == 0) & (WA['Age'] == '55-64')]) > 32:
    if len(WA[WA['Income per month'] == '€4001 – €5000']) > 80:
        index_to_delete = WA[(WA['Gender'] == 0) & (WA['Age'] == '55-64') & (WA['Income per month'] != '> €5000')& (WA['Income per month'] != '€1001 – €2000')].sample().index[0]
        Deletions_quota_WA.append(WA.loc[index_to_delete, 'ID'])
        WA.drop(index_to_delete, inplace=True)
    else:
        index_to_delete = WA[(WA['Gender'] == 0) & (WA['Age'] == '55-64') & (WA['Income per month'] != '> €5000') & (WA['Income per month'] != '€4001 – €5000')& (WA['Income per month'] != '€1001 – €2000')].sample().index[0]
        Deletions_quota_WA.append(WA.loc[index_to_delete, 'ID'])
        WA.drop(index_to_delete, inplace=True)
WA.reset_index(drop=True, inplace=True)

""" For Women 65+ """

while len(WA[(WA['Gender'] == 0) & (WA['Age'] == '65+')]) > 52:
    if len(WA[WA['Income per month'] == '€4001 – €5000']) > 80:
        index_to_delete = WA[(WA['Gender'] == 0) & (WA['Age'] == '65+') & (WA['Income per month'] != '> €5000')& (WA['Income per month'] != '€1001 – €2000')].sample().index[0]
        Deletions_quota_WA.append(WA.loc[index_to_delete, 'ID'])
        WA.drop(index_to_delete, inplace=True)
    else:
        index_to_delete = WA[(WA['Gender'] == 0) & (WA['Age'] == '65+') & (WA['Income per month'] != '> €5000') & (WA['Income per month'] != '€4001 – €5000')& (WA['Income per month'] != '€1001 – €2000')].sample().index[0]
        Deletions_quota_WA.append(WA.loc[index_to_delete, 'ID'])
        WA.drop(index_to_delete, inplace=True)
WA.reset_index(drop=True, inplace=True)

""" For Men 18-24 """

while len(WA[(WA['Gender'] == 1) & (WA['Age'] == '18-24')]) > 26:
    if len(WA[WA['Income per month'] == '€4001 – €5000']) > 80:
        index_to_delete = WA[(WA['Gender'] == 1) & (WA['Age'] == '18-24') & (WA['Income per month'] != '> €5000')& (WA['Income per month'] != '€1001 – €2000')].sample().index[0]
        Deletions_quota_WA.append(WA.loc[index_to_delete, 'ID'])
        WA.drop(index_to_delete, inplace=True)
    else:
        index_to_delete = WA[(WA['Gender'] == 1) & (WA['Age'] == '18-24') & (WA['Income per month'] != '> €5000') & (WA['Income per month'] != '€4001 – €5000')& (WA['Income per month'] != '€1001 – €2000')].sample().index[0]
        Deletions_quota_WA.append(WA.loc[index_to_delete, 'ID'])
        WA.drop(index_to_delete, inplace=True)
WA.reset_index(drop=True, inplace=True)

""" For Men 25-34 """

while len(WA[(WA['Gender'] == 1) & (WA['Age'] == '25-34')]) > 32:
    if len(WA[WA['Income per month'] == '€4001 – €5000']) > 80:
        index_to_delete = WA[(WA['Gender'] == 1) & (WA['Age'] == '25-34') & (WA['Income per month'] != '> €5000')& (WA['Income per month'] != '€1001 – €2000')].sample().index[0]
        Deletions_quota_WA.append(WA.loc[index_to_delete, 'ID'])
        WA.drop(index_to_delete, inplace=True)
    else:
        index_to_delete = WA[(WA['Gender'] == 1) & (WA['Age'] == '25-34') & (WA['Income per month'] != '> €5000') & (WA['Income per month'] != '€4001 – €5000')& (WA['Income per month'] != '€1001 – €2000')].sample().index[0]
        Deletions_quota_WA.append(WA.loc[index_to_delete, 'ID'])
        WA.drop(index_to_delete, inplace=True)
WA.reset_index(drop=True, inplace=True)

""" For Men 35-44 """

while len(WA[(WA['Gender'] == 1) & (WA['Age'] == '35-44')]) > 32:
    if len(WA[WA['Income per month'] == '€4001 – €5000']) > 80:
        index_to_delete = WA[(WA['Gender'] == 1) & (WA['Age'] == '35-44') & (WA['Income per month'] != '> €5000')& (WA['Income per month'] != '€1001 – €2000')].sample().index[0]
        Deletions_quota_WA.append(WA.loc[index_to_delete, 'ID'])
        WA.drop(index_to_delete, inplace=True)
    else:
        index_to_delete = WA[(WA['Gender'] == 1) & (WA['Age'] == '35-44') & (WA['Income per month'] != '> €5000') & (WA['Income per month'] != '€4001 – €5000')& (WA['Income per month'] != '€1001 – €2000')].sample().index[0]
        Deletions_quota_WA.append(WA.loc[index_to_delete, 'ID'])
        WA.drop(index_to_delete, inplace=True)
WA.reset_index(drop=True, inplace=True)

""" For Men 45-54 """

while len(WA[(WA['Gender'] == 1) & (WA['Age'] == '45-54')]) > 33:
    if len(WA[WA['Income per month'] == '€4001 – €5000']) > 80:
        index_to_delete = WA[(WA['Gender'] == 1) & (WA['Age'] == '45-54') & (WA['Income per month'] != '> €5000')& (WA['Income per month'] != '€1001 – €2000')].sample().index[0]
        Deletions_quota_WA.append(WA.loc[index_to_delete, 'ID'])
        WA.drop(index_to_delete, inplace=True)
    else:
        index_to_delete = WA[(WA['Gender'] == 1) & (WA['Age'] == '45-54') & (WA['Income per month'] != '> €5000') & (WA['Income per month'] != '€4001 – €5000')& (WA['Income per month'] != '€1001 – €2000')].sample().index[0]
        Deletions_quota_WA.append(WA.loc[index_to_delete, 'ID'])
        WA.drop(index_to_delete, inplace=True)
WA.reset_index(drop=True, inplace=True)

""" For Men 55-64 """

while len(WA[(WA['Gender'] == 1) & (WA['Age'] == '55-64')]) > 32:
    if len(WA[WA['Income per month'] == '€4001 – €5000']) > 80:
        index_to_delete = WA[(WA['Gender'] == 1) & (WA['Age'] == '55-64') & (WA['Income per month'] != '> €5000')& (WA['Income per month'] != '€1001 – €2000')].sample().index[0]
        Deletions_quota_WA.append(WA.loc[index_to_delete, 'ID'])
        WA.drop(index_to_delete, inplace=True)
    else:
        index_to_delete = WA[(WA['Gender'] == 1) & (WA['Age'] == '55-64') & (WA['Income per month'] != '> €5000') & (WA['Income per month'] != '€4001 – €5000')& (WA['Income per month'] != '€1001 – €2000')].sample().index[0]
        Deletions_quota_WA.append(WA.loc[index_to_delete, 'ID'])
        WA.drop(index_to_delete, inplace=True)
WA.reset_index(drop=True, inplace=True)

""" For Men 65+ """

while len(WA[(WA['Gender'] == 1) & (WA['Age'] == '65+')]) > 42:
    if len(WA[WA['Income per month'] == '€4001 – €5000']) > 80:
        index_to_delete = WA[(WA['Gender'] == 1) & (WA['Age'] == '65+') & (WA['Income per month'] != '> €5000')& (WA['Income per month'] != '€1001 – €2000')].sample().index[0]
        Deletions_quota_WA.append(WA.loc[index_to_delete, 'ID'])
        WA.drop(index_to_delete, inplace=True)
    else:
        index_to_delete = WA[(WA['Gender'] == 1) & (WA['Age'] == '65+') & (WA['Income per month'] != '> €5000') & (WA['Income per month'] != '€4001 – €5000')& (WA['Income per month'] != '€1001 – €2000')].sample().index[0]
        Deletions_quota_WA.append(WA.loc[index_to_delete, 'ID'])
        WA.drop(index_to_delete, inplace=True)
WA.reset_index(drop=True, inplace=True)



