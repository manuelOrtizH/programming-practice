/* Manuel Ortiz at 2023
Extracted from: https://leetcode.com/problems/capital-gainloss/ */

SELECT stock_name, 
SUM(IF(operation = 'BUY', -price, price)) AS capital_gain_loss
FROM Stocks
GROUP BY stock_name