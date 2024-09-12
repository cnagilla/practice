# Build stage
FROM mcr.microsoft.com/dotnet/sdk:6.0 AS build
ARG NUGET_URL="https://nuget.pkg.github.com/Org/index.json"
WORKDIR /src
COPY . .
WORKDIR "/src/Org.App.API"
RUN dotnet nuget add source --username admin --password pwd --store-password-in-clear-text --name github "${NUGET_URL}"
RUN dotnet restore
RUN dotnet publish -c Release -o /app

# Final stage
FROM mcr.microsoft.com/dotnet/aspnet:6.0
EXPOSE 8080
ENV ASPNETCORE_URLS=http://*:8080
ENV COMPlus_EnableDiagnostics=0
WORKDIR /app
COPY --from=build /app .
RUN groupadd -g 2000 org && useradd -u 1000 -g 2000 org && \
    chown -R org:org /app
USER org
ENTRYPOINT ["dotnet", "Org.App.API.dll"]
