
class DataWarehouseSql:

    @staticmethod
    def dim_products():
        return """
        SELECT	 
            p.productCode,
            p.productName,
            p.productVendor,
            p.productDescription,
            pl.productLine,
            pl.textDescription
        FROM products p 
            JOIN productlines pl 
            ON p.productLine = pl.productLine
        """
    
    @staticmethod
    def dim_customers():
        return """
        SELECT 
            customerNumber,
            customerName,
            phone,
            addressLine1,
            city,
            state,
            postalCode,
            country
        FROM
            customers
        """
    
    @staticmethod
    def dim_orders():
        return """
        SELECT 
            orderNumber,
            orderDate,
            requiredDate,
            shippedDate,
            status
        FROM
            orders
        """
    
    @staticmethod
    def dim_employees():
        return """
        SELECT 
            employeeNumber,
            CONCAT(lastName, ', ', firstName) fullName,
            jobTitle
        FROM
            employees
        """

    @staticmethod
    def dim_offices():
        return """
        SELECT 
            officeCode,
            city,
            state,
            country,
            territory
        FROM
            offices
        """
    
    @staticmethod
    def dim_time():
        return """
        SELECT 
            orderDate,
            YEAR(orderDate) year,
            MONTH(orderDate) month,
            DAY(orderDate) day
        FROM
            orders
        """
    
    @staticmethod
    def fact_sales():
        return """
        SELECT 	
            CONCAT(p.productCode, o.orderNumber) orderProductCode,
            p.productCode,
            p.productLine,
            o.orderNumber,
            c.customerNumber,
            e.employeeNumber,
            off.officeCode,
            o.orderDate,
            o.requiredDate,
            o.shippedDate,
            o.status,
            p.quantityInStock,
            p.buyPrice,
            p.MSRP,
            od.quantityOrdered,
            od.priceEach,
            od.orderLineNumber,
            CAST(od.priceEach * od.quantityOrdered AS DECIMAL(12,2)) AS itemProductRevenue,
            CAST((((od.priceEach - p.buyPrice) / p.buyPrice) * 100) AS DECIMAL(12,2)) AS markupPercentage,
            CAST(((quantityOrdered / quantityInStock)  * 100) AS DECIMAL(12,2))AS stockConversionRate,
            CAST((priceEach - MSRP) AS DECIMAL(12,2)) AS priceVariationFromMSRP
        FROM
            products p
            JOIN orderdetails od ON od.productCode = p.productCode 
            JOIN orders o ON o.orderNumber = od.orderNumber 
            JOIN customers c ON c.customerNumber = o.customerNumber 
            JOIN employees e ON e.employeeNumber = c.salesRepEmployeeNumber 
            JOIN offices off ON off.officeCode = e.officeCode
        """