---
title: Data Matching (Recordlinkage and Fuzzymatcher)
description: Small project of Recordlinkage and Fuzzymatcher.
categories:
  - EDA
#cover: '/assets/images/intro_api/api.png'
tags:
toc: true
toc_sticky: true
comments: true
excerpt: |
  Record Liking and Fuzzy Matching
#header:
#  image: /assets/images/logos/logo-text-8c3ba8a6.svg
---

# 1. Introduction

Record Linkage aka data matching/merging is to join the information from a variety of data sources. The `recordlinkage` and `fuzzymaker` are used for process of joining two data sets when they don't have a common unique identifier.

This problem is a common business challenge and difficult to solve in a systematic way due to the tremendous amount of data sets. A naive approach using vlookup function in Excel requests a lot of human intervention. To reduce that, `fuzzymatcher` and `recordlinkage` can be used.
1. `fuzzymatcher` allows us to match two pandas DataFrames using sqlite3 for finding potential matches and probabilistic record linkage for scoring those matches.
2. `recordlinkage` is a library to link records in or between data sources.

# 2. Problem
If trying to merge two datasets that comes from two separate sources, you must have some challenge of removing duplicates; like the contents are the same but a machine could not recognize that they are the same. For instance, a machine cannot recognize the duplicates that do not match exactly.

When machine recognizes that the data match:

![exact-match](/assets/images/data-matching/exact-match.png){:height="800px" width="700px"}  
| Fig1. Deterministic Matching |

This is called Deterministic matching. However, it happens that a part of data is mistyped or missing. Then, we use probability to match (Probabilistic matching). Using string distance algorithms like Levenshtein, Damerau-Levenshtein, Jaro-Winkler, q-gram, and cosine, we score a match to see how such matching is suitable.

![analogy](/assets/images/data-matching/analogy.png){:height="800px" width="600px"}  
| Fig2. Data Linkage/Matching Analogy |

Through the data-matching, Duplicates in the data can be eliminated.  

![dupls](/assets/images/data-matching/dupls.png){:height="800px" width="600px"}  
| Fig3. Eliminating Duplicates (Deduplication) |

The vlookup function in Excel requests exhaustive work, so using `fuzzymatcher` or `recordlinkage` is recommended.


# 3. Data
For exploring the data matching, US hospital data was used for the following challenges:

- Similar names of hospitals: to know they are different or the same (Saint Lukes, Saint Mary, etc.)
- Unclear addresses of hospitals: some hospitals located in urban areas have ambiguous addresses.
- A lot of assosiated clinics or facilities: hospitals tend to have many clinics and facilities associated and related nearby.
- Name changes: name changes of hospitals are common.
- Scalability: a thousands of medical facilities in the US is hard to scale.

The full data sets are available: [Medicare.gov](https://data.medicare.gov/Hospital-Compare/Hospital-General-Information/xubh-q36u) and [CMS.gov](https://www.cms.gov/Research-Statistics-Data-and-Systems/Statistics-Trends-and-Reports/Medicare-Provider-Charge-Data/Inpatient2016).
I used the cleaned version available [here]().


## 3.1. Importing packages


```python
import pandas as pd
from pathlib import Path
import fuzzywuzzy as fw # works at python 3.6 ver.
import fuzzymatcher as fm # works at python 3.6 ver.
import recordlinkage as rl# works at python 3.6 ver.

```

# 4. Fuzzymatcher
## 4.1. Loading the data



```python
hospital_accounts = pd.read_csv(
    'hospital_account_info.csv'
)
hospital_reimbursement = pd.read_csv(
    'hospital_reimbursement.csv'
)
```

US hospital account Data:


```python
hospital_accounts.head(2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Facility Name</th>
      <th>Address</th>
      <th>City</th>
      <th>State</th>
      <th>ZIP Code</th>
      <th>County Name</th>
      <th>Phone Number</th>
      <th>Hospital Type</th>
      <th>Hospital Ownership</th>
      <th>Acct_Name_Lookup</th>
    </tr>
    <tr>
      <th>Account_Num</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>10605</th>
      <td>SAGE MEMORIAL HOSPITAL</td>
      <td>STATE ROUTE 264 SOUTH 191</td>
      <td>GANADO</td>
      <td>AZ</td>
      <td>86505</td>
      <td>APACHE</td>
      <td>(928) 755-4541</td>
      <td>Critical Access Hospitals</td>
      <td>Voluntary non-profit - Private</td>
      <td>SAGE MEMORIAL HOSPITAL_STATE ROUTE 264 SOUTH 1...</td>
    </tr>
    <tr>
      <th>24250</th>
      <td>WOODRIDGE BEHAVIORAL CENTER</td>
      <td>600 NORTH 7TH STREET</td>
      <td>WEST MEMPHIS</td>
      <td>AR</td>
      <td>72301</td>
      <td>CRITTENDEN</td>
      <td>(870) 394-4113</td>
      <td>Psychiatric</td>
      <td>Proprietary</td>
      <td>WOODRIDGE BEHAVIORAL CENTER_600 NORTH 7TH STRE...</td>
    </tr>
  </tbody>
</table>
</div>



US reimbursement Data:


```python
hospital_reimbursement.head(2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Provider Name</th>
      <th>Provider Street Address</th>
      <th>Provider City</th>
      <th>Provider State</th>
      <th>Provider Zip Code</th>
      <th>Total Discharges</th>
      <th>Average Covered Charges</th>
      <th>Average Total Payments</th>
      <th>Average Medicare Payments</th>
      <th>Reimbursement_Name_Lookup</th>
    </tr>
    <tr>
      <th>Provider_Num</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>839987</th>
      <td>SOUTHEAST ALABAMA MEDICAL CENTER</td>
      <td>1108 ROSS CLARK CIRCLE</td>
      <td>DOTHAN</td>
      <td>AL</td>
      <td>36301</td>
      <td>118</td>
      <td>20855.61</td>
      <td>5026.19</td>
      <td>4115.52</td>
      <td>SOUTHEAST ALABAMA MEDICAL CENTER_1108 ROSS CLA...</td>
    </tr>
    <tr>
      <th>519118</th>
      <td>MARSHALL MEDICAL CENTER SOUTH</td>
      <td>2505 U S HIGHWAY 431 NORTH</td>
      <td>BOAZ</td>
      <td>AL</td>
      <td>35957</td>
      <td>43</td>
      <td>13289.09</td>
      <td>5413.63</td>
      <td>4490.93</td>
      <td>MARSHALL MEDICAL CENTER SOUTH_2505 U S HIGHWAY...</td>
    </tr>
  </tbody>
</table>
</div>



## 4.2. Joining the data
Since the columns have different names, we need to define which columns to match for the left and right DataFrames. In this case, the 'hospital_accounts' will be the left and the 'hospital_reimbursement' will be the right.


```python
# Columns to match on from df_left
left_on = ["Facility Name", "Address", "City", "State"]

# Columns to match on from df_right
right_on = [
    "Provider Name", "Provider Street Address", "Provider City",
    "Provider State"
]
```

Using function `fuzzy_left_join()`, I let the `fuzzymatcher` work on matching.


```python
# Now perform the match
# It will take several minutes to run on this data set
matched_results = fm.fuzzy_left_join(hospital_accounts,
                                               hospital_reimbursement,
                                               left_on,
                                               right_on,
                                               left_id_col='Account_Num',
                                               right_id_col='Provider_Num')
```

>**NOTE** For over 10 million combinations of the dataset, `fuzzymatcher` finds the best match for each combination, so it takes a while.

The DataFrame 'matched_results' contains all the data linked together as well as 'best_match_score' which shows the measure of the matching.


```python
matched_results.head(2)
```


<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>best_match_score</th>
      <th>__id_left</th>
      <th>__id_right</th>
      <th>Account_Num</th>
      <th>Facility Name</th>
      <th>Address</th>
      <th>City</th>
      <th>State</th>
      <th>ZIP Code</th>
      <th>County Name</th>
      <th>...</th>
      <th>Provider_Num</th>
      <th>Provider Name</th>
      <th>Provider Street Address</th>
      <th>Provider City</th>
      <th>Provider State</th>
      <th>Provider Zip Code</th>
      <th>Total Discharges</th>
      <th>Average Covered Charges</th>
      <th>Average Total Payments</th>
      <th>Average Medicare Payments</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-0.746613</td>
      <td>10605</td>
      <td>643595</td>
      <td>10605</td>
      <td>SAGE MEMORIAL HOSPITAL</td>
      <td>STATE ROUTE 264 SOUTH 191</td>
      <td>GANADO</td>
      <td>AZ</td>
      <td>86505</td>
      <td>APACHE</td>
      <td>...</td>
      <td>643595</td>
      <td>TYLER MEMORIAL HOSPITAL</td>
      <td>5950 STATE ROUTE 6 WEST</td>
      <td>TUNKHANNOCK</td>
      <td>PA</td>
      <td>18657</td>
      <td>18</td>
      <td>20482.94</td>
      <td>5783.22</td>
      <td>4929.22</td>
    </tr>
    <tr>
      <th>234</th>
      <td>-0.609873</td>
      <td>24250</td>
      <td>426767</td>
      <td>24250</td>
      <td>WOODRIDGE BEHAVIORAL CENTER</td>
      <td>600 NORTH 7TH STREET</td>
      <td>WEST MEMPHIS</td>
      <td>AR</td>
      <td>72301</td>
      <td>CRITTENDEN</td>
      <td>...</td>
      <td>426767</td>
      <td>CRISP REGIONAL HOSPITAL</td>
      <td>902 7TH STREET NORTH</td>
      <td>CORDELE</td>
      <td>GA</td>
      <td>31015</td>
      <td>18</td>
      <td>14655.94</td>
      <td>5680.28</td>
      <td>4899.39</td>
    </tr>
  </tbody>
</table>
</div>




## 4.3. Best and Worst Matches
The columns are rearranged for readability. The following data represent the top 3 best matches and the worst 3


```python
# Reorder the columns to make viewing easier
cols = [
    "best_match_score", "Facility Name", "Provider Name", "Address", "Provider Street Address",
    "Provider City", "City", "Provider State", "State"
]
```


```python
# Check the top 3 best matches
rearranged_best_matches=matched_results[cols].sort_values(by=['best_match_score'], ascending=False)
rearranged_best_matches.head(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>best_match_score</th>
      <th>Facility Name</th>
      <th>Provider Name</th>
      <th>Address</th>
      <th>Provider Street Address</th>
      <th>Provider City</th>
      <th>City</th>
      <th>Provider State</th>
      <th>State</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>78037</th>
      <td>3.090931</td>
      <td>RARITAN BAY MEDICAL CENTER PERTH AMBOY DIVISION</td>
      <td>RARITAN BAY MEDICAL CENTER PERTH AMBOY DIVISION</td>
      <td>530 NEW BRUNSWICK AVE</td>
      <td>530 NEW BRUNSWICK AVE</td>
      <td>PERTH AMBOY</td>
      <td>PERTH AMBOY</td>
      <td>NJ</td>
      <td>NJ</td>
    </tr>
    <tr>
      <th>533154</th>
      <td>2.799072</td>
      <td>ROBERT WOOD JOHNSON UNIVERSITY HOSPITAL</td>
      <td>ROBERT WOOD JOHNSON UNIVERSITY HOSPITAL</td>
      <td>ONE ROBERT WOOD JOHNSON PLACE</td>
      <td>ONE ROBERT WOOD JOHNSON PLACE</td>
      <td>NEW BRUNSWICK</td>
      <td>NEW BRUNSWICK</td>
      <td>NJ</td>
      <td>NJ</td>
    </tr>
    <tr>
      <th>78626</th>
      <td>2.785132</td>
      <td>AVERA MCKENNAN HOSPITAL &amp; UNIVERSITY HEALTH CE...</td>
      <td>AVERA MCKENNAN HOSPITAL &amp; UNIVERSITY HEALTH CE...</td>
      <td>1325 S CLIFF AVE  POST OFFICE BOX 5045</td>
      <td>1325 S CLIFF AVE  POST OFFICE BOX 5045</td>
      <td>SIOUX FALLS</td>
      <td>SIOUX FALLS</td>
      <td>SD</td>
      <td>SD</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Check the worst 3 matches
rearranged_worst_matches=matched_results[cols].sort_values(by=['best_match_score'],
                                  ascending=True)
rearranged_worst_matches.head(3)
# You can also use `tail()` from 'rearranged_best_matches'.
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>best_match_score</th>
      <th>Facility Name</th>
      <th>Provider Name</th>
      <th>Address</th>
      <th>Provider Street Address</th>
      <th>Provider City</th>
      <th>City</th>
      <th>Provider State</th>
      <th>State</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>426392</th>
      <td>-2.268231</td>
      <td>CENTRO MEDICO WILMA N VAZQUEZ</td>
      <td>BAPTIST MEDICAL CENTER EAST</td>
      <td>CARR. 2 KM 39.5    ROAD NUMBER 2 BO ALGARROBO</td>
      <td>400 TAYLOR ROAD</td>
      <td>MONTGOMERY</td>
      <td>VEGA BAJA</td>
      <td>AL</td>
      <td>PR</td>
    </tr>
    <tr>
      <th>83137</th>
      <td>-2.124071</td>
      <td>DOCTOR CENTER HOSPITAL SAN FERNANDO DE LA CARO...</td>
      <td>OVERLAKE HOSPITAL MEDICAL CENTER</td>
      <td>EDIF JESUS T PINEIRO AVE FERNANDEZ JUNCOS BO P...</td>
      <td>1035-116TH AVE NE</td>
      <td>BELLEVUE</td>
      <td>CAROLINA</td>
      <td>WA</td>
      <td>PR</td>
    </tr>
    <tr>
      <th>42545</th>
      <td>-2.106746</td>
      <td>HOSPITAL ONCOLOGICO DR ISAAC GONZALEZ MARTINEZ</td>
      <td>SCRIPPS MERCY HOSPITAL</td>
      <td>BO. MONACILLOS CARR 22 CENTRO MEDICO DE PUERTO...</td>
      <td>4077 5TH AVE</td>
      <td>SAN DIEGO</td>
      <td>SAN JUAN</td>
      <td>CA</td>
      <td>PR</td>
    </tr>
  </tbody>
</table>
</div>



As you can see, 'Provider State' and 'State' are different; meaning that some hospitals at different states (AL, WA, or CA) are mismatched with some hospitals at PR (Puerto Rico).

## Check the Threshold

Now let's find the threshold to collect the acceptible data that properly matched. When we see some of the matches with their scores $\leq$ 75:


```python
# Look at the matches below 0.75
matched_results[cols].query("best_match_score <= .75").sort_values(
    by=['best_match_score'], ascending=False).head(10)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>best_match_score</th>
      <th>Facility Name</th>
      <th>Provider Name</th>
      <th>Address</th>
      <th>Provider Street Address</th>
      <th>Provider City</th>
      <th>City</th>
      <th>Provider State</th>
      <th>State</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>179656</th>
      <td>0.745897</td>
      <td>HCA HOUSTON HEALTHCARE KINGWOOD</td>
      <td>KINGWOOD MEDICAL CENTER</td>
      <td>22999 US HWY 59</td>
      <td>22999 US HWY 59</td>
      <td>KINGWOOD</td>
      <td>KINGWOOD</td>
      <td>TX</td>
      <td>TX</td>
    </tr>
    <tr>
      <th>147070</th>
      <td>0.744798</td>
      <td>ADVENTIST HEALTH SONORA</td>
      <td>SONORA REGIONAL MEDICAL CENTER</td>
      <td>1000 GREENLEY ROAD</td>
      <td>1000 GREENLEY ROAD</td>
      <td>SONORA</td>
      <td>SONORA</td>
      <td>CA</td>
      <td>CA</td>
    </tr>
    <tr>
      <th>550827</th>
      <td>0.739983</td>
      <td>ADVENTHEALTH MANCHESTER</td>
      <td>MEMORIAL HOSPITAL</td>
      <td>210 MARIE LANGDON DRIVE</td>
      <td>210 MARIE LANGDON DRIVE</td>
      <td>MANCHESTER</td>
      <td>MANCHESTER</td>
      <td>KY</td>
      <td>KY</td>
    </tr>
    <tr>
      <th>404399</th>
      <td>0.739409</td>
      <td>UPMC KANE</td>
      <td>KANE COMMUNITY HOSPITAL</td>
      <td>4372 ROUTE 6</td>
      <td>4372 ROUTE 6</td>
      <td>KANE</td>
      <td>KANE</td>
      <td>PA</td>
      <td>PA</td>
    </tr>
    <tr>
      <th>399780</th>
      <td>0.738336</td>
      <td>MARSHFIELD MEDICAL CENTER - RICE LAKE</td>
      <td>LAKEVIEW MEDICAL CENTER</td>
      <td>1700 WEST STOUT STREET</td>
      <td>1700 WEST STOUT STREET</td>
      <td>RICE LAKE</td>
      <td>RICE LAKE</td>
      <td>WI</td>
      <td>WI</td>
    </tr>
    <tr>
      <th>477383</th>
      <td>0.736923</td>
      <td>TRINITY BETTENDORF</td>
      <td>UNITY POINT HEALTH TRINITY</td>
      <td>4500 UTICA RIDGE ROAD</td>
      <td>4500 UTICA RIDGE ROAD</td>
      <td>BETTENDORF</td>
      <td>BETTENDORF</td>
      <td>IA</td>
      <td>IA</td>
    </tr>
    <tr>
      <th>160318</th>
      <td>0.728097</td>
      <td>RUSH COPLEY MEDICAL CENTER</td>
      <td>COPLEY MEMORIAL HOSPITAL</td>
      <td>2000 OGDEN AVENUE</td>
      <td>2000 OGDEN AVENUE</td>
      <td>AURORA</td>
      <td>AURORA</td>
      <td>IL</td>
      <td>IL</td>
    </tr>
    <tr>
      <th>555173</th>
      <td>0.724772</td>
      <td>UNITYPOINT HEALTH - KEOKUK</td>
      <td>KEOKUK AREA HOSPITAL</td>
      <td>1600 MORGAN STREET</td>
      <td>1600 MORGAN STREET</td>
      <td>KEOKUK</td>
      <td>KEOKUK</td>
      <td>IA</td>
      <td>IA</td>
    </tr>
    <tr>
      <th>368685</th>
      <td>0.722856</td>
      <td>CALIFORNIA PACIFIC MEDICAL CTR-DAVIES CAMPUS HOSP</td>
      <td>CALIFORNIA PACIFIC MEDICAL CTR-PACIFIC CAMPUS ...</td>
      <td>601 DUBOCE AVENUE</td>
      <td>2333 BUCHANAN STREET</td>
      <td>SAN FRANCISCO</td>
      <td>SAN FRANCISCO</td>
      <td>CA</td>
      <td>CA</td>
    </tr>
    <tr>
      <th>431261</th>
      <td>0.720821</td>
      <td>KANSAS SPINE &amp; SPECIALTY HOSPITAL, LLC</td>
      <td>KANSAS HEART HOSPITAL</td>
      <td>3333 NORTH WEBB ROAD</td>
      <td>3601 NORTH WEBB ROAD</td>
      <td>WICHITA</td>
      <td>WICHITA</td>
      <td>KS</td>
      <td>KS</td>
    </tr>
  </tbody>
</table>
</div>



It shows that the data becomes more ambiguous below 0.75. The [CALIFORNIA PACIFIC MEDICAL CTR-DAVIES CAMPUS HOSP](https://www.sutterhealth.org/find-location/facility/cpmc-lab-davies-campus-castro-duboce) is different from [CALIFORNIA PACIFIC MEDICAL CTR-PACIFIC CAMPUS](https://www.sutterhealth.org/find-location/facility/cpmc-pacific-heights-outpatient-center-2333-buchanan-street).  
By checking your data, you need to find and set the proper threshold for collecting data.

Overall, `fuzzymatcher` is a useful tool to have for medium sized data sets (around 10,000) due to its computational time. However, it is easy to use.

# 5. Recordlinkage

Record Linkage Toolkit can clean, standardize data, and score similarity of data like `fuzzymatcher`, but it has additional capabilities:

- makes pairs of data by 'blocking' (`block()`) to limit the pool of potential matches and 'grouping' (`sortedneighbourhood()`) to cover the data with minor spelling mistakes.
- compares data with similarity scores for different types of data.
- provides Supervised and unsupervised classification algorithms for classifying data.

The trade-off is that it is a little more complicated to wrangle the results in order to do further validation. However, the steps are relatively standard pandas commands so do not let that intimidate you.


## 5.1. Loading the data with index_col

It needs to set the 'index_col' argument for indexing


```python
# Re-read in the data using the index_col
hospital_accounts = pd.read_csv(
    'hospital_account_info.csv',
    index_col='Account_Num'
)
hospital_reimbursement = pd.read_csv(
    'hospital_reimbursement.csv',
    index_col='Provider_Num'
)
```


```python
hospital_accounts.head(2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Facility Name</th>
      <th>Address</th>
      <th>City</th>
      <th>State</th>
      <th>ZIP Code</th>
      <th>County Name</th>
      <th>Phone Number</th>
      <th>Hospital Type</th>
      <th>Hospital Ownership</th>
    </tr>
    <tr>
      <th>Account_Num</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>10605</th>
      <td>SAGE MEMORIAL HOSPITAL</td>
      <td>STATE ROUTE 264 SOUTH 191</td>
      <td>GANADO</td>
      <td>AZ</td>
      <td>86505</td>
      <td>APACHE</td>
      <td>(928) 755-4541</td>
      <td>Critical Access Hospitals</td>
      <td>Voluntary non-profit - Private</td>
    </tr>
    <tr>
      <th>24250</th>
      <td>WOODRIDGE BEHAVIORAL CENTER</td>
      <td>600 NORTH 7TH STREET</td>
      <td>WEST MEMPHIS</td>
      <td>AR</td>
      <td>72301</td>
      <td>CRITTENDEN</td>
      <td>(870) 394-4113</td>
      <td>Psychiatric</td>
      <td>Proprietary</td>
    </tr>
  </tbody>
</table>
</div>




```python
hospital_reimbursement.head(2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Provider Name</th>
      <th>Provider Street Address</th>
      <th>Provider City</th>
      <th>Provider State</th>
      <th>Provider Zip Code</th>
      <th>Total Discharges</th>
      <th>Average Covered Charges</th>
      <th>Average Total Payments</th>
      <th>Average Medicare Payments</th>
    </tr>
    <tr>
      <th>Provider_Num</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>839987</th>
      <td>SOUTHEAST ALABAMA MEDICAL CENTER</td>
      <td>1108 ROSS CLARK CIRCLE</td>
      <td>DOTHAN</td>
      <td>AL</td>
      <td>36301</td>
      <td>118</td>
      <td>20855.61</td>
      <td>5026.19</td>
      <td>4115.52</td>
    </tr>
    <tr>
      <th>519118</th>
      <td>MARSHALL MEDICAL CENTER SOUTH</td>
      <td>2505 U S HIGHWAY 431 NORTH</td>
      <td>BOAZ</td>
      <td>AL</td>
      <td>35957</td>
      <td>43</td>
      <td>13289.09</td>
      <td>5413.63</td>
      <td>4490.93</td>
    </tr>
  </tbody>
</table>
</div>



## 5.2. Blocking
Blocking is nothing but a limiter of the size of comparisons. For instance, we want to compare the only hospitals that are in the same state. We can use this knowledge to setup a block on the state columns.

This will speed up the process, but adding some flexibility for minor spelling mistakes is important. Using `SortedNeighborhood()` function to clean the data


```python
# Build the indexer
indexer = rl.Index()
# Can use full or block
indexer.full()
indexer.block(left_on='State', right_on='Provider State')

# Use sortedneighbor as a good option if data is not clean
indexer.sortedneighbourhood(left_on='State', right_on='Provider State')
```

It may toss a warning of large number of data. With the `recordlinkage`, we have some flexibility to influence how many pairs are evaluated. By using full indexer all potential pairs are evaluated (which we know is over 14M pairs). I will come back to some of the other options in a moment. Let’s continue with the full index and see how it performs.

The next step is to build up all the potential candidates to check:

```python
candidates = indexer.index(hospital_accounts, hospital_reimbursement)
# Let's see how many matches we want to do
print(len(candidates))
```

    14399283


This quick check just confirmed the total number of comparisons. With the block on state, the 14,399,283 candidates will be filtered to only include those where the state values are the same. It may take longer to take care of minor spelling mistakes, but it is a reasonable trade-off.  

## 5.3. Comparing

Now that we have defined the left and right data sets and all the candidates, we can define how we want to perform the comparison logic using the `Compare()` function


```python
# Takes 3 minutes using the full index.
# 14s using sorted neighbor
# 7s using blocking
compare = rl.Compare()
compare.exact('City', 'Provider City', label='City')
compare.string('Facility Name',
               'Provider Name',
               threshold=0.85,
               label='Hosp_Name')
compare.string('Address',
               'Provider Street Address',
               method='jarowinkler',
               threshold=0.85,
               label='Hosp_Address')
features = compare.compute(candidates, hospital_accounts,
                           hospital_reimbursement)
```

We can define several options for how we want to compare the columns of data. In this specific example, we look for an exact match on the city. I have also shown some examples of string comparison along with the threshold and algorithm to use for comparison. In addition to these options, you can define your own or use numeric, dates and geographic coordinates. Refer to the documentation for more examples.

Regardless of which option you use, the result is a features DataFrame that looks like this:


```python
features
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>City</th>
      <th>Hosp_Name</th>
      <th>Hosp_Address</th>
    </tr>
    <tr>
      <th>Account_Num</th>
      <th>Provider_Num</th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="5" valign="top">10605</th>
      <th>537184</th>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>803181</th>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>450616</th>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>854377</th>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>560361</th>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>...</th>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th rowspan="5" valign="top">70226</th>
      <th>815904</th>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>746090</th>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>193062</th>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>834984</th>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>365095</th>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>



This DataFrame shows the results of all of the comparisons. There is one row for each row in the account and reimbursement DataFrames. The columns correspond to the comparisons we defined. 1 is a match and 0 is not.

## 5.4. Similarity Score

Given the large number of records with no matches, it is a little hard to see how many matches we might have. We can sum up the individual scores to see about the quality of the matches.


```python
# What are the score totals?
features.sum(axis=1).value_counts().sort_index(ascending=False)
```




    3.0      2285
    2.0       451
    1.0      7937
    0.0    988187
    dtype: int64



Now we know that there are 988,187 rows with no matching values
whatsoever. 7,937 rows have at least one match, 451 have 2 and 2,285 have 3 matches.

To make the rest of the analysis easier, let’s get all the records with 2 or 3 matches and add a total score:


```python
# Get the potential matches
potential_matches = features[features.sum(axis=1) > 1].reset_index()
```


```python
potential_matches['Score'] = potential_matches.loc[:, 'City':'Hosp_Address'].sum(axis=1)
potential_matches.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Account_Num</th>
      <th>Provider_Num</th>
      <th>City</th>
      <th>Hosp_Name</th>
      <th>Hosp_Address</th>
      <th>Score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>51216</td>
      <td>268781</td>
      <td>0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>55272</td>
      <td>556917</td>
      <td>1</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>87807</td>
      <td>854637</td>
      <td>1</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>51151</td>
      <td>783146</td>
      <td>1</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>11740</td>
      <td>260374</td>
      <td>1</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>3.0</td>
    </tr>
  </tbody>
</table>
</div>



Here is how to interpret the table. For the first row, Account_Num 55,272 and Provider_Num 556,917 match on city, hospital name and hospital address.

Let’s look at these two and see how close they are:


```python
hospital_accounts.loc[55272,:]
```




    Facility Name         SCOTTSDALE OSBORN MEDICAL CENTER
    Address                          7400 EAST OSBORN ROAD
    City                                        SCOTTSDALE
    State                                               AZ
    ZIP Code                                         85251
    County Name                                   MARICOPA
    Phone Number                            (480) 882-4004
    Hospital Type                     Acute Care Hospitals
    Hospital Ownership                         Proprietary
    Name: 55272, dtype: object




```python
hospital_reimbursement.loc[556917,:]
```




    Provider Name                SCOTTSDALE OSBORN MEDICAL CENTER
    Provider Street Address                 7400 EAST OSBORN ROAD
    Provider City                                      SCOTTSDALE
    Provider State                                             AZ
    Provider Zip Code                                       85251
    Total Discharges                                           62
    Average Covered Charges                               39572.2
    Average Total Payments                                6551.47
    Average Medicare Payments                             5451.89
    Name: 556917, dtype: object



Those look like good matches.

## 5.5. Joining

Now that we know the matches, we need to wrangle the data to make it easier to review all the data together. I am going to make a concatenated name and address lookup for each of these source DataFrames.


```python
# Add some convenience columns for comparing data
hospital_accounts['Acct_Name_Lookup'] = hospital_accounts[[
    'Facility Name', 'Address', 'City', 'State'
]].apply(lambda x: '_'.join(x), axis=1)
```


```python
hospital_reimbursement['Reimbursement_Name_Lookup'] = hospital_reimbursement[[
    'Provider Name', 'Provider Street Address', 'Provider City',
    'Provider State'
]].apply(lambda x: '_'.join(x), axis=1)
```


```python
reimbursement_lookup = hospital_reimbursement[['Reimbursement_Name_Lookup']].reset_index()
account_lookup = hospital_accounts[['Acct_Name_Lookup']].reset_index()
```


```python
account_lookup.head(2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Account_Num</th>
      <th>Acct_Name_Lookup</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>10605</td>
      <td>SAGE MEMORIAL HOSPITAL_STATE ROUTE 264 SOUTH 1...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>24250</td>
      <td>WOODRIDGE BEHAVIORAL CENTER_600 NORTH 7TH STRE...</td>
    </tr>
  </tbody>
</table>
</div>




```python
reimbursement_lookup.head(2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Provider_Num</th>
      <th>Reimbursement_Name_Lookup</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>839987</td>
      <td>SOUTHEAST ALABAMA MEDICAL CENTER_1108 ROSS CLA...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>519118</td>
      <td>MARSHALL MEDICAL CENTER SOUTH_2505 U S HIGHWAY...</td>
    </tr>
  </tbody>
</table>
</div>




```python
account_merge = potential_matches.merge(account_lookup, how='left')
account_merge.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Account_Num</th>
      <th>Provider_Num</th>
      <th>City</th>
      <th>Hosp_Name</th>
      <th>Hosp_Address</th>
      <th>Score</th>
      <th>Acct_Name_Lookup</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>51216</td>
      <td>268781</td>
      <td>0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>ST FRANCIS MEDICAL CENTER_2400 ST FRANCIS DRIV...</td>
    </tr>
    <tr>
      <th>1</th>
      <td>55272</td>
      <td>556917</td>
      <td>1</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>SCOTTSDALE OSBORN MEDICAL CENTER_7400 EAST OSB...</td>
    </tr>
    <tr>
      <th>2</th>
      <td>87807</td>
      <td>854637</td>
      <td>1</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>ORO VALLEY HOSPITAL_1551 EAST TANGERINE ROAD_O...</td>
    </tr>
    <tr>
      <th>3</th>
      <td>51151</td>
      <td>783146</td>
      <td>1</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>2.0</td>
      <td>ST. LUKE'S BEHAVIORAL HOSPITAL, LP_1800 EAST V...</td>
    </tr>
    <tr>
      <th>4</th>
      <td>11740</td>
      <td>260374</td>
      <td>1</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>3.0</td>
      <td>SUMMIT HEALTHCARE REGIONAL MEDICAL CENTER_2200...</td>
    </tr>
  </tbody>
</table>
</div>



The merge in the reimbursement data:


```python
# Let's build a dataframe to  compare
final_merge = account_merge.merge(reimbursement_lookup, how='left')
```


```python
cols = [
    'Account_Num', 'Provider_Num', 'Score', 'Acct_Name_Lookup',
    'Reimbursement_Name_Lookup'
]
```


```python
final_merge[cols].sort_values(by=['Account_Num', 'Score'], ascending=False)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Account_Num</th>
      <th>Provider_Num</th>
      <th>Score</th>
      <th>Acct_Name_Lookup</th>
      <th>Reimbursement_Name_Lookup</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2660</th>
      <td>94995</td>
      <td>825914</td>
      <td>3.0</td>
      <td>CLAIBORNE MEDICAL CENTER_1850 OLD KNOXVILLE HI...</td>
      <td>CLAIBORNE MEDICAL CENTER_1850 OLD KNOXVILLE HI...</td>
    </tr>
    <tr>
      <th>1975</th>
      <td>94953</td>
      <td>819181</td>
      <td>3.0</td>
      <td>LAKE CHARLES MEMORIAL HOSPITAL_1701 OAK PARK B...</td>
      <td>LAKE CHARLES MEMORIAL HOSPITAL_1701 OAK PARK B...</td>
    </tr>
    <tr>
      <th>1042</th>
      <td>94943</td>
      <td>680596</td>
      <td>3.0</td>
      <td>VALLEY PRESBYTERIAN HOSPITAL_15107 VANOWEN ST_...</td>
      <td>VALLEY PRESBYTERIAN HOSPITAL_15107 VANOWEN ST_...</td>
    </tr>
    <tr>
      <th>2305</th>
      <td>94923</td>
      <td>403151</td>
      <td>3.0</td>
      <td>UNIVERSITY COLO HEALTH MEMORIAL HOSPITAL CENTR...</td>
      <td>UNIVERSITY COLO HEALTH MEMORIAL HOSPITAL CENTR...</td>
    </tr>
    <tr>
      <th>2512</th>
      <td>94887</td>
      <td>752284</td>
      <td>2.0</td>
      <td>NEW YORK-PRESBYTERIAN BROOKLYN METHODIST HOSPI...</td>
      <td>NEW YORK METHODIST HOSPITAL_506 SIXTH STREET_B...</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2080</th>
      <td>10165</td>
      <td>188247</td>
      <td>3.0</td>
      <td>UTAH VALLEY HOSPITAL_1034 NORTH 500 WEST_PROVO_UT</td>
      <td>UTAH VALLEY HOSPITAL_1034 NORTH 500 WEST_PROVO_UT</td>
    </tr>
    <tr>
      <th>1825</th>
      <td>10090</td>
      <td>212069</td>
      <td>3.0</td>
      <td>CANONSBURG GENERAL HOSPITAL_100 MEDICAL BOULEV...</td>
      <td>CANONSBURG GENERAL HOSPITAL_100 MEDICAL BOULEV...</td>
    </tr>
    <tr>
      <th>2424</th>
      <td>10043</td>
      <td>140535</td>
      <td>3.0</td>
      <td>BETH ISRAEL DEACONESS HOSPITAL - PLYMOUTH_275 ...</td>
      <td>BETH ISRAEL DEACONESS HOSPITAL - PLYMOUTH_275 ...</td>
    </tr>
    <tr>
      <th>1959</th>
      <td>10020</td>
      <td>210657</td>
      <td>3.0</td>
      <td>ST FRANCIS MEDICAL CENTER_309 JACKSON STREET_M...</td>
      <td>ST FRANCIS MEDICAL CENTER_309 JACKSON STREET_M...</td>
    </tr>
    <tr>
      <th>1958</th>
      <td>10020</td>
      <td>121670</td>
      <td>2.0</td>
      <td>ST FRANCIS MEDICAL CENTER_309 JACKSON STREET_M...</td>
      <td>UNIVERSITY HEALTH CONWAY_4864 JACKSON STREET_M...</td>
    </tr>
  </tbody>
</table>
</div>

# 6. Deduplicates Remover with Recordlinkage
Another additional uses of the `Recordlinkage` is for finding duplicate records in a data set. The process is very similar to matching except you pass match a single DataFrame against itself.

## 6.1. Loading the data


```python
hospital_dupes = pd.read_csv(
    'hospital_account_dupes.csv',
    index_col='Account_Num')
```


```python
hospital_dupes.head(2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Facility Name</th>
      <th>Address</th>
      <th>City</th>
      <th>State</th>
      <th>ZIP Code</th>
      <th>County Name</th>
      <th>Phone Number</th>
      <th>Hospital Type</th>
      <th>Hospital Ownership</th>
    </tr>
    <tr>
      <th>Account_Num</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>71730</th>
      <td>SAGE MEMORIAL HOSPITAL</td>
      <td>STATE ROUTE 264 SOUTH 191</td>
      <td>GANADO</td>
      <td>AZ</td>
      <td>86505</td>
      <td>APACHE</td>
      <td>(928) 755-4541</td>
      <td>Critical Access Hospitals</td>
      <td>Voluntary non-profit - Private</td>
    </tr>
    <tr>
      <th>70116</th>
      <td>WOODRIDGE BEHAVIORAL CENTER</td>
      <td>600 NORTH 7TH STREET</td>
      <td>WEST MEMPHIS</td>
      <td>AR</td>
      <td>72301</td>
      <td>CRITTENDEN</td>
      <td>(870) 394-4113</td>
      <td>Psychiatric</td>
      <td>Proprietary</td>
    </tr>
  </tbody>
</table>
</div>



## 6.2. Blocking

Then create our indexer with a `sortedneighbourhood` block on State .


```python
# Deduping follows the same process, you just use 1 single dataframe
dupe_indexer = rl.Index()
dupe_indexer.sortedneighbourhood(left_on='State')
dupe_candidate_links = dupe_indexer.index(hospital_dupes)

```

## 6.3. Comparing

We should check for duplicates based on city, name and address:


```python
# Comparison step
compare_dupes = rl.Compare()
compare_dupes.string('City', 'City', threshold=0.85, label='City')
compare_dupes.string('Phone Number',
                     'Phone Number',
                     threshold=0.85,
                     label='Phone_Num')
compare_dupes.string('Facility Name',
                     'Facility Name',
                     threshold=0.80,
                     label='Hosp_Name')
compare_dupes.string('Address',
                     'Address',
                     threshold=0.85,
                     label='Hosp_Address')
dupe_features = compare_dupes.compute(dupe_candidate_links, hospital_dupes)
```

Because we are only comparing with a single DataFrame, the resulting DataFrame has an 'Account_Num_1' and 'Account_Num_2':


```python
dupe_features
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th></th>
      <th>City</th>
      <th>Phone_Num</th>
      <th>Hosp_Name</th>
      <th>Hosp_Address</th>
    </tr>
    <tr>
      <th>Account_Num_1</th>
      <th>Account_Num_2</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th rowspan="3" valign="top">26270</th>
      <th>28485</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>30430</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>43602</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th rowspan="2" valign="top">59585</th>
      <th>28485</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>30430</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>...</th>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th rowspan="5" valign="top">64029</th>
      <th>38600</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>35413</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>81525</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>82916</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>18907</th>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>

## 6.4. Similarity Score

```python
dupe_features.sum(axis=1).value_counts().sort_index(ascending=False)
```

    3.0         7
    2.0       206
    1.0      7859
    0.0    973205
    dtype: int64

```python
potential_dupes = dupe_features[dupe_features.sum(axis=1) > 2].reset_index()
potential_dupes['Score'] = potential_dupes.loc[:, 'City':'Hosp_Address'].sum(axis=1)
```


```python
potential_dupes.sort_values(by=['Score'], ascending=True)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Account_Num_1</th>
      <th>Account_Num_2</th>
      <th>City</th>
      <th>Phone_Num</th>
      <th>Hosp_Name</th>
      <th>Hosp_Address</th>
      <th>Score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>28494</td>
      <td>37949</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>74835</td>
      <td>77000</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>24549</td>
      <td>28485</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>70366</td>
      <td>52654</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>61685</td>
      <td>24849</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>5</th>
      <td>51567</td>
      <td>41166</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>3.0</td>
    </tr>
    <tr>
      <th>6</th>
      <td>26495</td>
      <td>41079</td>
      <td>1.0</td>
      <td>1.0</td>
      <td>0.0</td>
      <td>1.0</td>
      <td>3.0</td>
    </tr>
  </tbody>
</table>
</div>



These 7 records are potentially duplicates; having a high likelihood of being duplicated. Let’s look at them more deeply:


```python
# Take a look at one of the potential duplicates
hospital_dupes[hospital_dupes.index.isin([51567, 41166])]
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Facility Name</th>
      <th>Address</th>
      <th>City</th>
      <th>State</th>
      <th>ZIP Code</th>
      <th>County Name</th>
      <th>Phone Number</th>
      <th>Hospital Type</th>
      <th>Hospital Ownership</th>
    </tr>
    <tr>
      <th>Account_Num</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>41166</th>
      <td>ST VINCENT HOSPITAL</td>
      <td>835 S VAN BUREN ST</td>
      <td>GREEN BAY</td>
      <td>WI</td>
      <td>54301</td>
      <td>BROWN</td>
      <td>(920) 433-0111</td>
      <td>Acute Care Hospitals</td>
      <td>Voluntary non-profit - Church</td>
    </tr>
    <tr>
      <th>51567</th>
      <td>SAINT VINCENT HOSPITAL</td>
      <td>835 SOUTH VAN BUREN ST</td>
      <td>GREEN BAY</td>
      <td>WI</td>
      <td>54301</td>
      <td>BROWN</td>
      <td>(920) 433-0112</td>
      <td>Acute Care Hospitals</td>
      <td>Voluntary non-profit - Church</td>
    </tr>
  </tbody>
</table>
</div>

Such potential duplicates can be confirmed with further checks. Their names and addresses are similar and their phone numbers are off by one digit.

As you can see, this method can be a powerful and relatively easy tool to inspect your data and check for duplicate records.

# 7. Summary
Matching/Linking different datasets on text fields like names and addresses is a common challenge in data processing. This article provided two useful data linkage packages to match two data from separate sources.

The `fuzzymatcher` uses sqlite 3 to simply match two pandas DataFrames together, based on probabilistic scoring. If you have a larger data set or need to use more complex matching logic, then the `Recordlinkage` could be a better tool for  cleaning duplicates and joining data.
