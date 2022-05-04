--BANK MANAGER QUERRIES
/*
CREATE TABLE currency(
	curr_code VARCHAR(10),
	exch_rate FLOAT,
	PRIMARY KEY (curr_code)
);*/

--adds new currency***************************
/*INSERT INTO currency(curr_code, exch_rate)
VALUES({currency code}, {exchange rate});*/

--change exchange rate*************************
/*UPDATE currency
SET exch_rate = {exchange rate}
WHERE curr_code = {currency code};*/

--sets all clerk salaries**********************
/*UPDATE clerk 
SET salary = 2000;*/


--adds new customer
/*
INSERT INTO customer (id, firstN, lastN, phone, TC, Adress, cus_status)
VALUES({id}, {firstN}, {lastN}, {phone}, {TC}, {Adress}, 'NEW')*/

--deletes customer
/*DELETE customer 
WHERE id = {id};*/

--deletes customer
/*DELETE customer 
WHERE id = {id};*/

--adds new clerk
/*
INSERT INTO clerk (firstN, lastN, phoneNum)
VALUES({firstN}, {lastN}, {phoneNum})*/

--deletes clerk
/*DELETE clerk 
WHERE id = {id};*/


--Kredi ve gecikme faiz oran belirler.(?)
