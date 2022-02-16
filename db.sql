update auth_user
set is_superuser = 0
where id = 1;

update auth_user
set is_active = 1
where id = 1;

update rareapi_postreaction
set user_id = 4
where user_id = 3