import os
import numpy as np
import random
import sys
import pandas as pd
from sklearn import preprocessing
from keras.utils import to_categorical
from sklearn.model_selection import train_test_split

def ratings_to_num(array): # switch the rating to number
    np.place(array, array=='AAA', 0)
    np.place(array, array=='AA+', 1)
    np.place(array, array=='AA', 2)
    np.place(array, array=='AA-', 3)
    np.place(array, array=='A+', 4)
    np.place(array, array=='A', 5)
    np.place(array, array=='A-', 6)
    np.place(array, array=='BBB+', 7)
    np.place(array, array=='BBB', 8)
    np.place(array, array=='BBB-', 9)
    np.place(array, array=='BB+', 10)
    np.place(array, array=='BB', 11)
    np.place(array, array=='BB', 12)
    np.place(array, array=='BB-', 13)
    np.place(array, array=='B+', 14)
    np.place(array, array=='B', 15)
    np.place(array, array=='B-', 16)
    np.place(array, array=='CCC+', 17)
    np.place(array, array=='CCC', 18)
    np.place(array, array=='CCC-', 19)
    np.place(array, array=='CC', 20)
    np.place(array, array=='C', 21)
    np.place(array, array=='D', 22)
    np.place(array, array=='SD', 23)
    np.place(array, array=='N.M.', 24)
    return array


def data_clean_image(sector, tyear, MASK = True, shuffle = False):
    info = [
         'Global Company Key',
         'Data Date',
         'Fiscal Year',
         'Fiscal Quarter',
         'Industry Format',
         'Level of Consolidation - Company Interim Descriptor',
         'Population Source',
         'Data Format',
         'Ticker Symbol',
         'Company Name',
         'ISO Currency Code',
         'Calendar Data Year and Quarter',
         'Fiscal Data Year and Quarter',
         'Active/Inactive Status Marker'
    ]
    sequence = [
        'Assets - Total',
        'Current Assets - Total',
        'Cash and Short-Term Investments',
        'Cash',
        'Short-Term Investments- Total',
        'Receivables - Total',
        'Receivables (Net) - Utility',
        'Receivables - Trade',
        'Receivables - Current Other incl Tax Refunds',
        'Unbilled Receivables - Quarterly',
        'Receivables - Estimated Doubtful',
        'Inventories - Total',
        'Inventories',
        'Inventory - Raw Materials',
        'Inventory - Work in Process',
        'Inventory - Finished Goods',
        'Inventory - Other',
        'Current Assets - Other - Total',


        'Current Assets - Other - Utility',
        'Current Deferred Tax Asset',
        'Non-Current Assets - Total',
        'Property Plant and Equipment - Total (Net)',
        'Property, Plant and Equipment - Total (Gross) - Quarterly',
        'Contributions In Aid Of Construction',
        'Depreciation, Depletion and Amortization (Accumulated)',
        'Total Long-term Investments',
        'Investment and Advances - Equity',
        'Investment and Advances - Other',
        'Assets - Other - Total',
        'Intangible Assets - Total',
        'Other Intangibles',
        'Goodwill (net)',
        'Other Long-term Assets',
        'Other Assets - Utility',
        'Deferred Tax Asset - Long Term',
        'Liabilities and Stockholders Equity - Total',
        'Liabilities - Total and Noncontrolling Interest',
        'Liabilities - Total',
        'Current Liabilities - Total',
        'Debt in Current Liabilities',
        'Long-Term Debt Due in One Year',
        'Notes Payable',
        'Deferred Revenue - Current',

        'Accounts Payable - Utility',


        'Account Payable/Creditors - Trade',


        'Income Taxes Payable',
        'Current Liabilities - Other - Total',
        'Accrued Expenses',
        'Current Liabilities - Other',
        'Current Deferred Tax Liability',
        'Long-Term Liabilities (Total)',
        'Long-Term Debt - Total',
        'Debt (Pollution Control Obligations)',
        'Debt (Debentures) - Utility',
        'Debt (Mortgage Bonds)',
        'Debt (Other Long-Term)',
        'Deferred Revenue - Long-term',
        'Liabilities - Other',
        'Liabilities - Other - Excluding Deferred Revenue',
        'Deferred Taxes and Investment Tax Credit',
        'Deferred Taxes - Balance Sheet',

        'Noncontrolling Interest - Redeemable - Balance Sheet',
        'Stockholders Equity - Total',
        'Preferred/Preference Stock (Capital) - Total',
        'Preferred/Preference Stock - Redeemable',
        'Preferred/Preference Stock - Nonredeemable',
        'Common/Ordinary Equity - Total',
        'Common Equity - Total - Utility',
        'Common/Ordinary Stock (Capital)',
        'Capital Surplus/Share Premium Reserve',
        'Retained Earnings',
        'Unadjusted Retained Earnings',
        'Paid In Capital - Other - Utility',
        'Treasury Stock - Total (All Capital)',
        'Stockholders Equity > Parent > Index Fundamental > Quarterly',
        'Noncontrolling Interests - Total - Balance Sheet',
        'Noncontrolling Interests - Nonredeemable - Balance Sheet',
        'Other Stockholders- Equity Adjustments',

        'Premium On Common Stock - Utility',
        'Premium On Preferred Stock - Utility',
        'Premium On Preference Stock - Utility',
        'Premium On Subsidiary Preferred Stock - Utility',
        'Accumulated Depreciation of RE Property',
        'Depr/Amort of Property',
        'Total RE Property',
        'Nonperforming Assets - Total',
        'Net Charge-Offs',
        'Assets Level1 (Quoted Prices)',
        'Assets Level2 (Observable)',
        'Total Fair Value Changes including Earnings',
        'Assets Level3 (Unobservable)',
        'Assets Netting & Other Adjustments',
        'Total Fair Value Assets',
        'Liabilities Level1 (Quoted Prices)',
        'Liabilities Level2 (Observable)',

        'Liabilities Level3 (Unobservable)',
        'Liabilities Netting & Other Adjustments',
        'Total Fair Value Liabilities',
        'Working Capital (Balance Sheet)',
        'Invested Capital - Total - Quarterly',
        'Deferred Compensation',
        'Common Shares Issued',
        'Total Shares Repurchased - Quarter',
        'Common Shares Outstanding',
        'Nonred Pfd Shares Outs (000) - Quarterly',
        'Redeem Pfd Shares Outs (000)',
        'Carrying Value',
        'Preference Stock At Carrying Value - Utility',
        'Preferred Stock At Carrying Value - Utility',
        'Subsidiary Preferred Stock At Carrying Value - Utility',
        'Repurchase Price - Average per share Quarter',
        'Common ESOP Obligation - Total',
        'Preferred ESOP Obligation - Non-Redeemable',
        'Preferred ESOP Obligation - Redeemable',
        'Preferred ESOP Obligation - Total',
        'Dividend Rate - Assumption (%)',
        'Options - Fair Value of Options Granted',
        'Life of Options - Assumption (# yrs)',
        'Risk Free Rate - Assumption (%)',
        'Volatility - Assumption (%)',
        'Risk-Adjusted Capital Ratio - Tier 1',
        'Risk-Adjusted Capital Ratio - Tier 2',
        'Risk-Adjusted Capital Ratio - Combined',

        'Revenue - Total',
        'Sales/Turnover (Net)',
        'Gain/Loss on Sale of Property',

        'Operating Income - Total - Utility',
        'Operating Expense- Total',
        'Cost of Goods Sold',
        'Selling, General and Administrative Expenses',
        'Research and Development Expense',
        'Maintenance Expense - Total',
        'Operating Income Before Depreciation - Quarterly',
        'Depreciation and Amortization - Total',
        'Amortization of Goodwill',
        'Operating Income After Depreciation - Quarterly',
        'Gross Income (Income Before Interest Charges)',
        'Foreign Exchange Income (Loss)',
        'Interest Income - Total (Financial Services)',

        'Special Items',
        'Special Items - Utility',

        'Interest and Related Expense- Total',
        'Interest Expense - Total (Financial Services)',

        'Excise Taxes',
        'Nonoperating Income (Net) - Other',
        'Non-Operating Income (Expense) - Total',
        'Pretax Income',

        'Income Taxes - Total',

        'Income Taxes - Deferred',

        'Income before Extraordinary Items and Noncontrolling Interests',
        'Noncontrolling Interest - Income Account',
        'Net Income before Extraordinary Items After Noncontrolling Interest',
        'Income Before Extraordinary Items',
        'Dividends - Preferred/Preference',
        'Preferred Dividend Requirements',
        'Preference Dividend Requirements - Utility',
        'Subsidiary Preferred Dividends - Utility',
        'Income Before Extraordinary Items - Available for Common',
        'Common Stock Equivalents - Dollar Savings',
        'Income Before Extraordinary Items - Adjusted for Common Stock Equivalents',
        'Extraordinary Items and Discontinued Operations',
        'Extraordinary Items',
        'Discontinued Operations',

        'Net Income (Loss)',

        'Dilution Adjustment',
        'Dilution Available - Excluding Extraordinary Items',
        'Common Shares Used to Calculate Earnings Per Share - Basic',
        'Com Shares for Diluted EPS',
        'Common Shares Used to Calculate Earnings Per Share - 12 Months Moving',
        'Earnings Per Share (Basic) - Excluding Extraordinary Items',
        'Earnings Per Share (Diluted) - Excluding Extraordinary items',
        'Earnings Per Share (Basic) - Excluding Extraordinary Items - 12 Months Moving',
        'Earnings Per Share (Diluted) - Excluding Extraordinary Items - 12 Months Moving',
        'Earnings Per Share (Basic) - Including Extraordinary Items',
        'Earnings Per Share (Diluted) - Including Extraordinary Items',
        'Earnings Per Share from Operations',
        'Earnings Per Share - Diluted - from Operations',
        'Earnings Per Share from Operations - 12 Months Moving',
        'Earnings Per Share - Diluted - from Operations - 12MM',


        'As Reported Core - After-tax',
        'As Reported Core - Basic EPS Effect',
        'As Reported Core - Diluted EPS Effect',

        'Comp Inc - Beginning Net Income',
        'Comp Inc - Currency Trans Adj',
        'Comp Inc - Derivative Gains/Losses',
        'Comp Inc - Other Adj',
        'Comp Inc - Minimum Pension Adj',
        'Comp Inc - Securities Gains/Losses',
        'Comprehensive Income - Total',
        'Comprehensive Income - Parent',
        'Comprehensive Income - Noncontrolling Interest',
        'Accumulated Other Comprehensive Income (Loss)',
        'Accum Other Comp Inc - Unreal G/L Ret Int in Sec Assets',
        'Accum Other Comp Inc - Marketable Security Adjustments',
        'Accum Other Comp Inc - Cumulative Translation Adjustments',
        'Accum Other Comp Inc - Min Pension Liab Adj',
        'Accum Other Comp Inc - Derivatives Unrealized Gain/Loss',
        'Accum Other Comp Inc - Other Adjustments',

        'Net Interest Income (Tax Equivalent)',
        'Net Interest Margin',
        'Accounting Changes - Cumulative Effect',
        'Equity in Earnings (I/S) - Unconsolidated Subsidiaries',
        'Funds From Operations (REIT)',
        'Gain/Loss on Ineffective Hedges',
        'Provision for Loan/Asset Losses',
        'Reserve for Loan/Asset Losses',
        'Treasury Stock - Number of Common Shares',
        'Stock Compensation Expense',
        'After-tax stock compensation',
        'Income Before Extra Items - Adj for Common Stock Equivalents - 12MM',
        'Reversal - Restructruring/Acquisition Pretax',
        'Reversal - Restructruring/Acquisition Aftertax',
        'Reversal - Restructuring/Acq Basic EPS Effect',
        'Reversal - Restructuring/Acq Diluted EPS Effect',
        'Reversal - Restructruring/Acquisition Aftertax 12MM',
        'Reversal - Restructuring/Acq Basic EPS Effect 12MM',
        'Reversal - Restructuring/Acq Diluted EPS Effect 12MM',
        'Implied Option Expense',
        'Implied Option EPS Basic',
        'Implied Option EPS Diluted',
        'Implied Option Expense - 12mm',
        'Implied Option EPS Basic 12MM',
        'Implied Option EPS Diluted 12MM',
        'Implied Option Expense Preliminary',
        'Implied Option EPS Basic Preliminary',
        'Implied Option EPS Diluted Preliminary',
        'Implied Option 12MM EPS Basic Preliminary',
        'Implied Option 12MM EPS Diluted Preliminary',
        'Nonrecurring Income Taxes - After-tax',
        'Nonrecurring Income Taxes Basic EPS Effect',
        'Nonrecurring Income Taxes Diluted EPS Effect',

        'Acquisition/Merger Pretax',
        'Acquisition/Merger After-Tax',
        'Acquisition/Merger Basic EPS Effect',
        'Acquisition/Merger Diluted EPS Effect',
        'Gain/Loss Pretax',
        'Gain/Loss After-Tax',
        'Gain/Loss Basic EPS Effect',
        'Gain/Loss Diluted EPS Effect',
        'Gain/Loss on Sale (Core Earnings Adjusted) Pretax',
        'Gain/Loss on Sale (Core Earnings Adjusted) After-tax',
        'Gain/Loss on Sale (Core Earnings Adjusted) After-tax 12MM',
        'Gain/Loss on Sale (Core Earnings Adjusted) Basic EPS Effect',
        'Gain/Loss on Sale (Core Earnings Adjusted) Basic EPS Effect 12MM',
        'Gain/Loss on Sale (Core Earnings Adjusted) Diluted EPS',
        'Gain/Loss on Sale (Core Earnings Adjusted) Diluted EPS Effect 12MM',
        'Impairment of Goodwill Pretax',
        'Impairment of Goodwill After-tax',
        'Impairment of Goodwill Basic EPS Effect',
        'Impairment of Goodwill Diluted EPS Effect',
        'Impairments of Goodwill AfterTax - 12mm',
        'Impairment of Goodwill Basic EPS Effect 12MM',
        'Impairments Diluted EPS - 12mm',
        'Settlement (Litigation/Insurance) Pretax',
        'Settlement (Litigation/Insurance) After-tax',
        'Settlement (Litigation/Insurance) Basic EPS Effect',
        'Settlement (Litigation/Insurance) Diluted EPS Effect',
        'Settlement (Litigation/Insurance) AfterTax - 12mm',
        'Settlement (Litigation/Insurance) Basic EPS Effect 12MM',
        'Settlement (Litigation/Insurance) Diluted EPS Effect 12MM',
        'Restructuring Cost Pretax',
        'Restructuring Cost After-tax',
        'Restructuring Cost Basic EPS Effect',
        'Restructuring Cost Diluted EPS Effect',
        'Writedowns Pretax',
        'Writedowns After-tax',
        'Writedowns Basic EPS Effect',
        'Writedowns Diluted EPS Effect',
        'Extinguishment of Debt Pretax',
        'Extinguishment of Debt After-tax',
        'Extinguishment of Debt Basic EPS Effect',
        'Extinguishment of Debt Diluted EPS Effect',
        'In Process R&D',
        'In Process R&D Expense After-tax',
        'In Process R&D Expense Basic EPS Effect',
        'In Process R&D Expense Diluted EPS Effect',
        'Other Special Items Pretax',
        'Other Special Items After-tax',
        'Other Special Items Basic EPS Effect',
        'Other Special Items Diluted EPS Effect',

        'S&P Core Earnings',
        'S&P Core Earnings EPS Basic',
        'S&P Core Earnings EPS Diluted',
        'S&P Core Earnings 12MM',
        'S&P Core Earnings EPS Basic 12MM',
        'S&P Core Earnings EPS Diluted 12MM',
        'S&P Core Earnings - Preliminary',
        'S&P Core Earnings EPS Basic - Preliminary',
        'S&P Core Earnings EPS Diluted - Preliminary',
        'S&P Core Earnings 12MM - Preliminary',
        'S&P Core 12MM EPS - Basic - Preliminary',
        'S&P Core Earnings 12MM EPS Diluted - Preliminary',

        'Core Pension Adjustment',
        'Core Pension Adjustment Basic EPS Effect',
        'Core Pension Adjustment Diluted EPS Effect',
        'Pension Core Adjustment - 12mm',
        'Core Pension Adjustment Basic EPS Effect 12MM',
        'Core Pension Adjustment Diluted EPS Effect 12MM',
        'Core Pension Adjustment Preliminary',
        'Core Pension Adjustment Basic EPS Effect Preliminary',
        'Core Pension Adjustment Diluted EPS Effect Preliminary',
        'Core Pension Adjustment 12MM Basic EPS Effect Preliminary',
        'Core Pension Adjustment 12MM Diluted EPS Effect Preliminary',
        'Core Pension Interest Adjustment Pretax',
        'Core Pension Interest Adjustment After-tax',
        'Core Pension Interest Adjustment Basic EPS Effect',
        'Core Pension Interest Adjustment Diluted EPS Effect',
        'Core Pension Interest Adjustment Pretax Preliminary',
        'Core Pension Interest Adjustment After-tax Preliminary',
        'Core Pension Interest Adjustment Basic EPS Effect Preliminary',
        'Core Pension Interest Adjustment Diluted EPS Effect Preliminary',
        'Core Pension w/o Interest Adjustment Pretax',
        'Core Pension w/o Interest Adjustment After-tax',
        'Core Pension w/o Interest Adjustment Basic EPS Effect',
        'Core Pension w/o Interest Adjustment Diluted EPS Effect',
        'Core Pension w/o Interest Adjustment Pretax Preliminary',
        'Core Pension w/o Interest Adjustment After-tax Preliminary',
        'Core Pension w/o Interest Adjustment Basic EPS Effect Preliminary',
        'Core Pension w/o Interest Adjustment Diluted EPS Effect Preliminary',
        'Core Post Retirement Adjustment',
        'Core Post Retirement Adjustment Basic EPS Effect',
        'Core Post Retirement Adjustment Diluted EPS Effect',
        'Core Post Retirement Adjustment 12MM',
        'Core Post Retirement Adjustment Basic EPS Effect 12MM',
        'Core Post Retirement Adjustment Diluted EPS Effect 12MM',
        'Core Post Retirement Adjustment Preliminary',
        'Core Post Retirement Adjustment Basic EPS Effect Preliminary',
        'Core Post Retirement Adjustment Diluted EPS Effect Preliminary',
        'Core Post Retirement Adjustment 12MM Basic EPS Effect Preliminary',
        'Core Post Retirement Adjustment 12MM Diluted EPS Effect Preliminary',

        'Order backlog',
        'Interest Accrued',
    ]
    data = pd.read_excel('./SectorData/'+ sector + '.xlsx')
    #print ratings.head()

    #READ DATA
    ratings = pd.read_excel('./SectorData/'+ sector + 'Rating.xlsx')

    data = data[info+sequence] # rearrange the cols
    
    #data.dropna(how = 'all', axis =1, inplace = True)
    #data.dropna(how = 'any', axis =1, thresh = data.shape[0] * 0.05, inplace = True)
    data.fillna(0, inplace = True)

    if data.shape[1] < 360 + len(info):
        addlist = [str(i) for i in range(360 + len(info) - data.shape[1])]
        data = data.reindex(columns= (data.columns.tolist()+addlist), fill_value=0)
    

    features_col = data.columns.tolist()
    #print (data.shape)
    

    matched=pd.merge(data,ratings, how='inner', on=['Data Date','Global Company Key']) #matched the ratings and the date 
    #print ('matched shape:', matched.shape)

    matched['Data Date'] = matched['Data Date'].astype('str')
    #matched.to_csv("match.csv",index=False,sep=',')


    matched1 = matched.dropna(subset=['S&P Domestic Long Term Issuer Credit Rating'])

    matched1.index = range(matched1.shape[0])



    #matched1.to_csv("match1.csv",index=False,sep=',')

    data = matched1[features_col[14:]]   #extract the features part
    mask = data.isnull()        #mark those null part as mask
    data.fillna(0, inplace=True)    #make the feature no Null

    ratings = matched1[['S&P Domestic Long Term Issuer Credit Rating']]  #get the ratings

    #NORMALIZING
    x = data.values #returns a numpy array
    min_max_scaler = preprocessing.MinMaxScaler()
    x_scaled = min_max_scaler.fit_transform(x)
    df = pd.DataFrame(x_scaled, index = data.index, columns = data.columns)
    #print (df)

    ratings_np = ratings.values
    data_np = df.values
    mask_np =  mask.values


    labels = ratings_to_num(ratings_np)

    # MASKS to 0 and 1
    mask_np=np.logical_not(mask_np)
    mask_np=mask_np.astype(float)


    labels=labels.astype(int)
    data_np=data_np.astype(float)

    if MASK:
        
        features = np.concatenate((data_np,mask_np),1) #combine mask and data
    else:
        
        features = data_np

    y = 30
    #Features = pd.DataFrame(features, columns = )
    features = np.reshape(features, (features.shape[0], y, int(360/y)))
    
    Ratings =  pd.DataFrame(to_categorical(ratings))

    if shuffle:
        train_x, test_x, train_y, test_y = train_test_split(features, Ratings, test_size=0.06, random_state=42)
        #test_year=(np.random.random(len(matched1['Data Date'])) >0.8)
        print ('training: ', train_x.shape, train_y.shape)
        print ('Test size: ', test_x.shape, test_y.shape)
        return train_x, train_y.values, test_x, test_y.values
    else:
        test_year=matched1['Data Date'].map(lambda x: int(x[:4])== tyear)

    #

        train_x = features[~test_year]
        train_y = Ratings[~test_year]
        test_x = features[test_year]
        test_y = Ratings[test_year]

        print ('training: ', train_x.shape, train_y.shape)
        print ('Test size: ', test_x.shape, test_y.shape)
        

        return train_x, train_y.values, test_x, test_y.values
    



if __name__ == "__main__":
    train_x, train_y, test_x, test_y = data_clean_image('Energy', tyear=2015, MASK = False, shuffle = False)
    print (train_y)


