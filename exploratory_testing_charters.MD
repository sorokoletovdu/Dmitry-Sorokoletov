### Charter-001
**Explore** main feauture of the application  
**with** multiple expence and income inputs  
**to discover** calculating of the balance

### Charter-002
**Explore** charts   
**with** adding expenses in all default categories  
**to discover** user interface changes

### Charter-003
**Explore** balance detalization   
**with** opening balance detalization screen  
**to discover** how all operations are displayed

### Charter-004
**Explore** adding of new operation  
**with** operations of different values  
**to discover** how expenses and incomes are added

### Charter-005
**Explore** filter by date  
**with** choosing different parameters  
**to discover** how charts and balance detalization changes

### Charter-006
**Explore** search field  
**with** key category names  
**to discover** output of searching results

### Charter-007
**Explore** money transfer  
**with** adding a new transfer from cash to card  
**to discover** how the transer is displayed

2. During application usage were found the following bugs (or defects):
* at choosing balance detalization for all accounts "transfer operations" weren't in the list;
* the sum of the category percents is not 100;
* chart sectors with 1% have the different size;
* some categories have 0% even there were added operations, so value type should be changes from int to float in order to display percentage more accurate;
* at choosing date in calendar there is no possibility to jump several years ago or months ago, user has to swipe all months till the necessary date. As a result it makes impossible to open the chart for the period that was 4 years ago, for example;
* at choosing date in the calendar if we swipe several months and press cancel, than open another screen and return to the calendar, it didn't reset to current date;
* at filling in note with symbols more than a screen width the text in the note is shown partly, the note field didn't expand;
* at searching "Car" the results show "From 'Cash'" even there is no substring "Car" in any results.

3. The Charters are already prioritised by user experience path. So, as a user I will check the main functionality of the app and then go deeper to the aaditional functions.

4. The testing of each charter will take 15-20 minutes.

5. The main risks I will need to mitigate are:
* data destorsion;
* data loss;
* data leackage.