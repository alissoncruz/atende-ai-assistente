FROM maven:3.9.9-eclipse-temurin-21 AS build
WORKDIR /src
COPY . .
RUN mvn -B -ntp -pl apps/api -am package -DskipTests

FROM eclipse-temurin:21-jre
WORKDIR /app
COPY --from=build /src/apps/api/target/atendeai-api-0.1.0-SNAPSHOT.jar /app/atendeai-api.jar
CMD ["java", "-jar", "/app/atendeai-api.jar"]
