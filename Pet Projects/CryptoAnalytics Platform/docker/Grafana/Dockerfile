FROM grafana/grafana:main

USER root

# Ensure the directory exists
RUN mkdir -p /etc/grafana/provisioning/datasources

# Add the ClickHouse datasource configuration
COPY Grafana/clickhouse-datasource.yml /etc/grafana/provisioning/datasources/

# Add the home dashboard
#COPY grafana/dashboard/home.json /usr/share/grafana/public/dashboards/

# Copy and install the ClickHouse datasource plugin
COPY Grafana/grafana-clickhouse-datasource-4.5.0.linux_amd64.zip /var/lib/grafana/plugins/

# Install unzip and extract the plugin
RUN if command -v apt-get > /dev/null; then \
        apt-get update && apt-get install -y unzip; \
    elif command -v apk > /dev/null; then \
        apk add --no-cache unzip; \
    fi && \
    unzip /var/lib/grafana/plugins/grafana-clickhouse-datasource-4.5.0.linux_amd64.zip -d /var/lib/grafana/plugins/ && \
    rm /var/lib/grafana/plugins/grafana-clickhouse-datasource-4.5.0.linux_amd64.zip

USER grafana