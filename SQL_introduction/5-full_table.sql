-- Query to get the CREATE TABLE statement for first_table
SELECT table_name, create_statement
FROM (
    SELECT 
        table_name, 
        table_type, 
        engine, 
        version, 
        row_format, 
        table_rows, 
        avg_row_length, 
        data_length, 
        max_data_length, 
        index_length, 
        data_free, 
        auto_increment, 
        create_time, 
        update_time, 
        check_time, 
        table_collation, 
        checksum, 
        create_options, 
        table_comment, 
        TABLE_NAME AS table_name, 
        TABLE_SCHEMA AS table_schema, 
        TABLE_COLLATION AS table_collation, 
        CREATE_TIME AS create_time, 
        UPDATE_TIME AS update_time, 
        TABLE_ROWS AS table_rows, 
        AVG_ROW_LENGTH AS avg_row_length, 
        DATA_LENGTH AS data_length, 
        MAX_DATA_LENGTH AS max_data_length, 
        INDEX_LENGTH AS index_length, 
        DATA_FREE AS data_free, 
        AUTO_INCREMENT AS auto_increment, 
        CREATE_OPTIONS AS create_options, 
        TABLE_COMMENT AS table_comment, 
        ENGINE AS engine, 
        VERSION AS version, 
        ROW_FORMAT AS row_format, 
        CHECKSUM AS checksum, 
        TABLE_SCHEMA, 
        CONCAT('CREATE TABLE `', TABLE_NAME, '` (\n', GROUP_CONCAT(CONCAT('  `', COLUMN_NAME, '` ', COLUMN_TYPE, IF(IS_NULLABLE = 'NO', ' NOT NULL', ''), IF(COLUMN_DEFAULT IS NOT NULL, CONCAT(' DEFAULT ', COLUMN_DEFAULT), ''), IF(EXTRA = '', '', CONCAT(' ', EXTRA)), '\n') ORDER BY ORDINAL_POSITION SEPARATOR ','), '\n) ENGINE=', ENGINE, ' DEFAULT CHARSET=', SUBSTRING_INDEX(TABLE_COLLATION, '_', 1), ' COLLATE=', TABLE_COLLATION) AS create_statement
    FROM 
        information_schema.TABLES 
    LEFT JOIN 
        information_schema.COLUMNS 
    ON 
        TABLES.TABLE_SCHEMA = COLUMNS.TABLE_SCHEMA 
        AND TABLES.TABLE_NAME = COLUMNS.TABLE_NAME 
    WHERE 
        TABLES.TABLE_SCHEMA = 'hbtn_0c_0' 
        AND TABLES.TABLE_NAME = 'first_table'
    GROUP BY 
        TABLES.TABLE_NAME
) AS derived;
