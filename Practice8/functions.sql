CREATE OR REPLACE FUNCTION search_pattern(p text)
RETURNS TABLE(name varchar, phone varchar)
AS $$
BEGIN
 RETURN QUERY
 SELECT username, phone
 FROM contacts
 WHERE username ILIKE '%' || p || '%'
 OR phone ILIKE '%' || p || '%';
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION get_page(lim int, offs int)
RETURNS TABLE(name varchar, phone varchar)
AS $$
BEGIN
 RETURN QUERY
 SELECT username, phone
 FROM contacts
 LIMIT lim OFFSET offs;
END;
$$ LANGUAGE plpgsql;