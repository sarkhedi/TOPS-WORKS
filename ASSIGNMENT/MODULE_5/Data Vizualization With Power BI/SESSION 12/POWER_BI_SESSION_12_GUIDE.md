# Power BI Session 12 - Advanced Visuals Guide

આ ફોલ્ડરમાં બધા 5 Tasks માટે જરૂરી CSV ડેટાસેટ્સ સીધા જ બનાવી દીધા છે (કોઈ Python સ્ક્રિપ્ટ વગર). તમે આ ફાઇલોને સીધી જ Power BI માં Import કરીને visual બનાવી શકો છો.

---

## 📁 ઉપલબ્ધ CSV ડેટાસેટ્સ:
1. `task1_food_delivery_monthly_orders.csv`
2. `task2_ipl_fantasy_funnel.csv`
3. `task3_flipkart_city_orders.csv`
4. `task4_movies_box_office_2023.csv`
5. `task5_indian_apps_dau_session_duration.csv`

---

## 📊 Visuals બનાવાની વિગતવાર રીત (Step-by-Step Instructions)

### Task 1: Food Delivery Monthly Orders - Waterfall Chart
- **Visual Name:** **Waterfall Chart** (વિઝ્યુઅલાઈઝેશન પેનમાં Waterfall આઇકન પસંદ કરો)
- **Data Source:** [task1_food_delivery_monthly_orders.csv](file:///e:/TOPS-WORKS/ASSIGNMENT/MODULE_5/Data%20Vizualization%20with%20Power%20BI/SESSION%2012/task1_food_delivery_monthly_orders.csv)
- **Field Settings:**
  - **Category:** `Month`
  - **Breakdown (Optional):** `App` (જો Zomato, Swiggy, Uber Eats વાઈઝ વધારો-ઘટાડો બતાવવો હોય)
  - **Y-axis:** `Orders` (Sum of Orders)
- **Key Insight:** જાન્યુઆરીથી જૂન સુધી કુલ ઓર્ડર્સમાં થયેલો ક્રમિક વધારો (Net positive change) સ્પષ્ટ રીતે દેખાશે.

---

### Task 2: IPL Fantasy League User Conversion - Funnel Chart
- **Visual Name:** **Funnel Chart**
- **Data Source:** [task2_ipl_fantasy_funnel.csv](file:///e:/TOPS-WORKS/ASSIGNMENT/MODULE_5/Data%20Vizualization%20with%20Power%20BI/SESSION%2012/task2_ipl_fantasy_funnel.csv)
- **Field Settings:**
  - **Category:** `Stage`
  - **Values:** `User_Count`
- **Sorting Tip:**
  - `Stage` કોલમ સિલેક્ટ કરીને **Sort by Column** માં જઈને `Stage_Order` પસંદ કરો જેથી સ્ટેજ ક્રમમાં દેખાય:
    1. *Visited App* (5,00,000)
    2. *Registered* (3,20,000)
    3. *Created Team* (2,10,000)
    4. *Joined League* (1,40,000)
    5. *Made Payment* (85,000)

---

### Task 3: Flipkart City-wise Orders - Map Visual
- **Visual Name:** **Map** (અથવા Filled Map)
- **Data Source:** [task3_flipkart_city_orders.csv](file:///e:/TOPS-WORKS/ASSIGNMENT/MODULE_5/Data%20Vizualization%20with%20Power%20BI/SESSION%2012/task3_flipkart_city_orders.csv)
- **Field Settings:**
  - **Location:** `City`
  - **Bubble size:** `Order_Volume`
  - **Tooltip:** `State`, `Average_Order_Value_INR`
- **Highest & Lowest Analysis:**
  - **Highest Order Counts:** Bengaluru, Delhi, Mumbai (સૌથી મોટા બબલ)
  - **Lowest Order Counts:** Agartala, Gangtok, Shimla (સૌથી નાના બબલ)

---

### Task 4: 2023 Movies Box Office Collections - Treemap Visual
- **Visual Name:** **Treemap**
- **Data Source:** [task4_movies_box_office_2023.csv](file:///e:/TOPS-WORKS/ASSIGNMENT/MODULE_5/Data%20Vizualization%20with%20Power%20BI/SESSION%2012/task4_movies_box_office_2023.csv)
- **Field Settings:**
  - **Category:** `Genre` (Action, Drama, Comedy, Animation, વગેરે)
  - **Details:** `Movie_Name` (જેથી દરેક Genre અંદર અલગ અલગ મૂવીના બ્લોક દેખાય)
  - **Values:** `Box_Office_Collection_Crores` (Sum)
- **Drill-down Feature:** તમે Genre પર ક્લિક કરીને અંદરના વ્યક્તિગત મૂવીઝને જોઈ શકો છો.

---

### Task 5: Top 10 Indian Apps - Scatter Chart Visual (Outlier Analysis)
- **Visual Name:** **Scatter Chart**
- **Data Source:** [task5_indian_apps_dau_session_duration.csv](file:///e:/TOPS-WORKS/ASSIGNMENT/MODULE_5/Data%20Vizualization%20with%20Power%20BI/SESSION%2012/task5_indian_apps_dau_session_duration.csv)
- **Field Settings:**
  - **Values:** `App_Name`
  - **X-axis:** `Daily_Active_Users_Millions` (સરેરાશ દૈનિક સક્રિય યુઝર્સ)
  - **Y-axis:** `Avg_Session_Duration_Minutes` (સરેરાશ સત્ર અવધિ)
  - **Size (Optional):** `Monthly_Downloads_Millions`
  - **Data Labels:** Turn **ON** (Format pane -> Data labels -> Enable)

#### Outliers ની ઓળખ અને સમજૂતી (Explanation of Outliers):
1. **Outlier 1: Instagram (Extreme High Session Duration)**
   - *Data:* 360M DAU, **52.0 Minutes** Average Session Duration.
   - *Explanation:* Instagram સામાન્ય એપ્સ (જેમ કે Flipkart 12.5 min, Zomato 8.5 min) કરતાં ખુબ જ વધારે સેશન ડ્યુરેશન ધરાવે છે. આનું કારણ અનંત રીલ્સ સ્ક્રોલિંગ (algorithmic infinite video feed) અને હાઈ એંગેજમેન્ટ છે.
2. **Outlier 2: PhonePe (High DAU, Exceptionally Low Session Duration)**
   - *Data:* 165M DAU, **3.5 Minutes** Average Session Duration.
   - *Explanation:* PhonePe પાસે ખૂબ મોટો દૈનિક યુઝરબેઝ છે પરંતુ સેશન સમય અત્યંત ઓછો (3.5 મિનિટ) છે. કારણ કે તે એક ફિનટેક/યુટિલિટી એપ છે જ્યાં યુઝર ફક્ત QR કોડ સ્કેન કરવા કે પેમેન્ટ કરવા માટે 1-2 મિનિટ માટે જ એપ ખોલે છે.
3. **Outlier 3: WhatsApp (Massive Scale Outlier)**
   - *Data:* **480M DAU** સાથે ભારતની સૌથી વધુ ઉપયોગમાં લેવાતી રોજિંદી કોમ્યુનિકેશન એપ.
