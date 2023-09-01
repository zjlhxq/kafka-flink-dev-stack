package org.example;

// Purpose: Read products and transactions data from Kafka topics,
//          joins both datasets into enriched purchases,
//          and writes results to a new Kafka topic.
// Author:  Gary A. Stafford
// Date: 2022-12-28

import com.schema.avro.demo.Product;
import com.schema.avro.demo.Purchase;
import com.schema.avro.demo.PurchaseEnriched;
import org.apache.flink.api.common.eventtime.WatermarkStrategy;
import org.apache.flink.connector.base.DeliveryGuarantee;
import org.apache.flink.connector.kafka.sink.KafkaRecordSerializationSchema;
import org.apache.flink.connector.kafka.sink.KafkaSink;
import org.apache.flink.connector.kafka.source.KafkaSource;
import org.apache.flink.connector.kafka.source.enumerator.initializer.OffsetsInitializer;
import org.apache.flink.formats.avro.registry.confluent.ConfluentRegistryAvroDeserializationSchema;
import org.apache.flink.formats.avro.registry.confluent.ConfluentRegistryAvroSerializationSchema;
import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import org.apache.flink.table.api.Table;
import org.apache.flink.table.api.bridge.java.StreamTableEnvironment;


import java.io.IOException;
import java.io.InputStream;
import java.util.Properties;

public class JoinStreams {

    public static void main(String[] args) throws Exception {
        Properties prop = getProperties();
        flinkKafkaPipeline(prop);
    }

    private static Properties getProperties() {
        Properties prop = new Properties();

        try (InputStream propsInput =
                     JoinStreams.class.getClassLoader().getResourceAsStream("config.properties")) {
            prop.load(propsInput);
            return prop;
        } catch (IOException e) {
            e.printStackTrace();
        }
        return prop;
    }

    public static void flinkKafkaPipeline(Properties prop) throws Exception {

        StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
        StreamTableEnvironment tableEnv = StreamTableEnvironment.create(env);

        // assumes PLAINTEXT authentication
        String schemaRegistryUrl = prop.getProperty("SCHEMA_REGISTRY_URL");
        KafkaSource<Product> productSource = KafkaSource.<Product>builder()
                .setBootstrapServers(prop.getProperty("BOOTSTRAP_SERVERS"))
                .setTopics(prop.getProperty("PRODUCTS_TOPIC"))
                .setGroupId("flink_join_demo")
                .setStartingOffsets(OffsetsInitializer.earliest())
                .setValueOnlyDeserializer(ConfluentRegistryAvroDeserializationSchema.forSpecific(
                        Product.class, schemaRegistryUrl))
                .build();

        DataStream<Product> productsStream = env.fromSource(
                productSource, WatermarkStrategy.noWatermarks(), "Kafka Products Source");

        tableEnv.createTemporaryView("products", productsStream);

        KafkaSource<Purchase> purchasesSource = KafkaSource.<Purchase>builder()
                .setBootstrapServers(prop.getProperty("BOOTSTRAP_SERVERS"))
                .setTopics(prop.getProperty("PURCHASES_TOPIC"))
                .setGroupId("flink_join_demo")
                .setStartingOffsets(OffsetsInitializer.earliest())
                .setValueOnlyDeserializer(ConfluentRegistryAvroDeserializationSchema.forSpecific(
                        Purchase.class, schemaRegistryUrl))
                .build();

        DataStream<Purchase> purchasesStream = env.fromSource(
                purchasesSource, WatermarkStrategy.noWatermarks(), "Kafka Purchases Source");

        tableEnv.createTemporaryView("purchases", purchasesStream);

        Table result =
                tableEnv.sqlQuery(
                        "SELECT " +
                                "purchases.transactionTime, " +
                                "purchases.transactionTime, " +
                                "purchases.transactionId, " +
                                "purchases.productId, " +
                                "products.category, " +
                                "products.item, " +
                                "products.size, " +
                                "products.cogs, " +
                                "products.price, " +
                                "products.containsFruit, " +
                                "products.containsVeggies, " +
                                "products.containsNuts, " +
                                "products.containsCaffeine, " +
                                "purchases.price, " +
                                "purchases.quantity, " +
                                "purchases.isMember, " +
                                "purchases.memberDiscount, " +
                                "purchases.addSupplements, " +
                                "purchases.supplementPrice, " +
                                "purchases.totalPurchase " +
                                "FROM " +
                                "products " +
                                "JOIN purchases " +
                                "ON products.productId = purchases.productId"
                );

        DataStream<PurchaseEnriched> purchasesEnrichedTable = tableEnv.toDataStream(result,
                PurchaseEnriched.class);

        KafkaSink<PurchaseEnriched> sink = KafkaSink.<PurchaseEnriched>builder()
                .setBootstrapServers(prop.getProperty("BOOTSTRAP_SERVERS"))
                .setRecordSerializer(KafkaRecordSerializationSchema.builder()
                        .setTopic(prop.getProperty("PURCHASES_ENRICHED_TOPIC"))
                        .setValueSerializationSchema(ConfluentRegistryAvroSerializationSchema.forSpecific(
                                PurchaseEnriched.class,
                                PurchaseEnriched.getClassSchema().getFullName() + "-value",
                                schemaRegistryUrl))
                        .build()
                ).setDeliveryGuarantee(DeliveryGuarantee.AT_LEAST_ONCE)
                .build();

        purchasesEnrichedTable.sinkTo(sink);

        env.executeAsync("Flink Streaming Join Demo");

    }
}
