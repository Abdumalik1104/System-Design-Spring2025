// Fan-in (входящие зависимости)
MATCH (c:Component)<-[:DEPENDS_ON]-(d:Component)
RETURN c.name AS Component, COUNT(d) AS FanIn
ORDER BY Component;

// Fan-out (исходящие зависимости)
MATCH (c:Component)-[:DEPENDS_ON]->(d:Component)
RETURN c.name AS Component, COUNT(d) AS FanOut
ORDER BY Component;

// Instability (I)
MATCH (c:Component)
OPTIONAL MATCH (c)<-[:DEPENDS_ON]-(in:Component)
WITH c, COUNT(in) AS FanIn
OPTIONAL MATCH (c)-[:DEPENDS_ON]->(out:Component)
WITH c, FanIn, COUNT(out) AS FanOut
RETURN c.name AS Component, FanIn, FanOut, 
       CASE WHEN FanIn + FanOut = 0 THEN 0 
            ELSE toFloat(FanOut) / (FanIn + FanOut) 
       END AS Instability
ORDER BY Component;