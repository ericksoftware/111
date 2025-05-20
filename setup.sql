

CREATE TABLE IF NOT EXISTS task (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name VARCHAR(50),
  summary VARCHAR(255),
  description TEXT,
  is_done BOOLEAN DEFAULT 0
);

INSERT INTO task (name, summary, description) VALUES
  ('Task 1', 'Summary of Task 1', 'Description of Task 1'),
  ('Task 2', 'Summary of Task 2', 'Description of Task 2'),
  ('Task 3', 'Summary of Task 3', 'Description of Task 3'),
  ('Task 4', 'Summary of Task 4', 'Description of Task 4'),
  ('Task 5', 'Summary of Task 5', 'Description of Task 5');

