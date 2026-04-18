CREATE OR REPLACE PROCEDURE upsert_user(n varchar, p varchar)
LANGUAGE plpgsql
AS $$
BEGIN
 IF EXISTS (SELECT 1 FROM contacts WHERE username=n) THEN
   UPDATE contacts SET phone=p WHERE username=n;
 ELSE
   INSERT INTO contacts(username, phone) VALUES(n,p);
 END IF;
END;
$$;


CREATE