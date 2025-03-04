// Удаляем все данные
MATCH (n) DETACH DELETE n;

// Создаём узлы (компоненты)
CREATE (auth:Component {name: 'AuthService'})
CREATE (user:Component {name: 'UserService'})
CREATE (db:Component {name: 'Database'})
CREATE (course:Component {name: 'CourseService'})
CREATE (notif:Component {name: 'NotificationService'})
CREATE (email:Component {name: 'EmailService'});

// Создаём связи (зависимости)
MATCH (auth:Component {name: 'AuthService'})
MATCH (user:Component {name: 'UserService'})
MATCH (db:Component {name: 'Database'})
MATCH (course:Component {name: 'CourseService'})
MATCH (notif:Component {name: 'NotificationService'})
MATCH (email:Component {name: 'EmailService'})

CREATE (auth)-[:DEPENDS_ON]->(user)
CREATE (user)-[:DEPENDS_ON]->(db)
CREATE (course)-[:DEPENDS_ON]->(db)
CREATE (course)-[:DEPENDS_ON]->(user)
CREATE (notif)-[:DEPENDS_ON]->(user)
CREATE (notif)-[:DEPENDS_ON]->(email);