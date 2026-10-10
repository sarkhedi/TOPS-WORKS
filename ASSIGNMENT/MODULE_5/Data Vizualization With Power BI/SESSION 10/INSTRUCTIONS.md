# Session 10 - Basic Visuals in Power BI (Step-by-Step Guide)

આ ફોલ્ડરમાં બધા જ 5 ટાસ્ક માટે સીધા Power BI માં ઈમ્પોર્ટ કરી શકાય તેવા **CSV ડેટા સેટ્સ (Ready-to-Use)** બનાવી દીધા છે:

---

## 📁 ઉપલબ્ધ CSV ફાઈલો:
1. `ipl_matches.csv` - Task 1 (Table Visual)
2. `zomato_ratings.csv` - Task 2 (Matrix Visual)
3. `flipkart_users.csv` - Task 3 (Card Visual)
4. `spotify_subscriptions.csv` - Task 4 (KPI Visual)
5. `bookmyshow_bookings.csv` - Task 5 (Bar / Column Chart with Top N)

---

## 🛠️ દરેક ટાસ્ક કેવી રીતે બનાવવો (Step-by-Step Instructions)

### Task 1: IPL Cricket Matches - Table Visual
- **ડેટા ફાઈલ:** `ipl_matches.csv`
- **Power BI માં સ્ટેપ્સ:**
  1. **Get Data** -> **Text/CSV** -> `ipl_matches.csv` પસંદ કરીને **Load** કરો.
  2. Visualizations pane માંથી **Table** visual પસંદ કરો.
  3. Columns સેક્શનમાં નીચે મુજબ ફિલ્ડ્સ Drag & Drop કરો:
     - `Team_Name`
     - `Runs_Scored` (જો Sum આવે તો યોગ્ય છે, અથવા Don't summarize પણ રાખી શકાય)
     - `Match_Date`

---

### Task 2: Zomato Restaurant Ratings - Matrix Visual
- **ડેટા ફાઈલ:** `zomato_ratings.csv`
- **Power BI માં સ્ટેપ્સ:**
  1. **Get Data** -> **Text/CSV** -> `zomato_ratings.csv` પસંદ કરીને **Load** કરો.
  2. Visualizations pane માંથી **Matrix** visual પસંદ કરો.
  3. ફિલ્ડ્સ આ મુજબ ગોઠવો:
     - **Rows:** `City`
     - **Columns:** `Cuisine`
     - **Values:** `Rating` -> ડ્રોપડાઉન એરો પર ક્લિક કરીને **Average** પસંદ કરો (જેથી પ્રતિ City અને Cuisine ની સરેરાશ રેટિંગ દેખાય).

---

### Task 3: Flipkart Active Users - Card Visual
- **ડેટા ફાઈલ:** `flipkart_users.csv`
- **Power BI માં સ્ટેપ્સ:**
  1. **Get Data** -> **Text/CSV** -> `flipkart_users.csv` લોડ કરો.
  2. Visualizations pane માંથી **Card** visual પસંદ કરો.
  3. **Fields:** `User_ID` ફિલ્ડ મૂકો અને તેનું એગ્રીગેશન **Count (Distinct)** અથવા **Count** રાખો.
  4. **Filters Pane** માં:
     - `Account_Status` ફિલ્ડને **Filters on this visual** માં Drag કરો.
     - **Basic filtering** માં ફક્ત **Active** પર ચેકમાર્ક (Tick) કરો.
  5. કાર્ડ પર ફક્ત Active users ની કુલ સંખ્યા (Total Active Users = 19) દેખાશે.

---

### Task 4: Spotify Premium Subscriptions - KPI Visual
- **ડેટા ફાઈલ:** `spotify_subscriptions.csv`
- **Power BI માં સ્ટેપ્સ:**
  1. **Get Data** -> **Text/CSV** -> `spotify_subscriptions.csv` લોડ કરો.
  2. Visualizations pane માંથી **KPI** visual પસંદ કરો.
  3. ફિલ્ડ્સ આ મુજબ સેટ કરો:
     - **Value (Indicator):** `Premium_Subscriptions`
     - **Trend axis:** `Date` (અથવા `Month_Name`)
     - **Target:** `Previous_Month_Subscriptions` (અથવા `Target_Subscriptions`)
  4. આ visual તમને Current month નો ગ્રોથ અને અગાઉના મહિના કરતાં વધારો કે ઘટાડો (Green / Red indicator સાથે) બતાવશે.

---

### Task 5: BookMyShow Top 5 Movies - Bar / Column Chart (Top N Filter)
- **ડેટા ફાઈલ:** `bookmyshow_bookings.csv`
- **Power BI માં સ્ટેપ્સ:**
  1. **Get Data** -> **Text/CSV** -> `bookmyshow_bookings.csv` લોડ કરો.
  2. Visualizations pane માંથી **Clustered Column Chart** અથવા **Clustered Bar Chart** પસંદ કરો.
  3. ફિલ્ડ્સ આ મુજબ મૂકો:
     - **X-axis (અથવા Y-axis):** `Movie_Name`
     - **Y-axis (અથવા X-axis):** `Tickets_Sold` (Sum of Tickets_Sold)
  4. **Top 5 Filter લગાવવા માટે:**
     - ચાર્ટ સિલેક્ટ રાખીને જમણી બાજુ **Filters pane** ખોલો.
     - **Filters on this visual** ની અંદર `Movie_Name` પર ક્લિક કરો.
     - **Filter type** માં **Top N** પસંદ કરો.
     - **Show items:** **Top** અને બોક્સમાં **5** લખો.
     - **By value:** બોક્સમાં `Tickets_Sold` ફિલ્ડ drag કરીને મૂકો.
     - નીચે **Apply filter** બટન પર ક્લિક કરો.
  5. હવે ચાર્ટમાં ફક્ત સૌથી વધુ ટિકિટ વેચાયેલી ટોપ 5 મૂવીઝ દેખાશે.
