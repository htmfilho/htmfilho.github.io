---
layout: post
title: "Table Generation Strategy Revised"
date: 2009-05-24 05:30:00 +0200
categories: database enterprise application java
---

The JEE platform (EJB 3.0) offers, since its previous version (EJB 2.1), a feature to generate database tables during the application deployment. This feature is currently part of the Java Persistence API (JPA), which can be used even outside the JEE environment, like in desktop applications. My case is exactly a desktop application where I’m using an embedded database to simplify as much as possible the application installation and configuration.

When I started working with this <a href="http://developers.sun.com/javadb/">embedded database</a> I have configured my persistence.xml file to “create” the database tables during the deployment time, based on annotations made in the entity classes. This option generates a DDL (Data Definition Language) file that is processed by the JPA framework to generate the tables. Unfortunately, if you change your entity classes, this strategy won’t update the existing tables, creating inconsistencies with the data model. Unfortunately, the application will crash. There are other two options: a) “delete and create”, which will drop the entire database structure to be created again; and b) “do nothing” and let the developer find a way to manage the database structure. “delete and create” keeps the consistency between entity classes and data model but it loses all the data persisted so far. It might be useful for tests, but the developer should remember to change this option when delivering a new version to end-users, which is the addition of one more point of failure. “do nothing” implies in more work for developers, who will take the responsibility to manage the data structure. Based on the two shameful possibilities (“create” and “delete and create”), “do nothing” seems to be the best and unique option available for serious projects.

Today I’m using the option “do nothing”, keeping in mind my constant concern for simplifying the life of end users when installing and using the application. So, every time the application is started I check if the database exists. If not, I execute a ddl script bundled inside the main jar file. I’m using the following code:

{% highlight java %}
public static void main(String[] args) {
  {...}
  boolean applicationPropertiesLoaded = false;
  int attempts = 0;
  do {
    try {
      attempts++;
      loadApplicationProperties();
      applicationPropertiesLoaded = true;
    }
    catch(Exception e) {
      logger.warning("Application properties"+
                     "not found. Trying to create the database");
      createDatabase();
      if(attempts == 2) {
        logger.severe("Problem to load application properties.");
      }
    }
  } while(!applicationPropertiesLoaded || (attempts < 2));
  {...}
}
{% endhighlight %}

The code above tries to access the database, executing a basic operation like loading the application properties. If the database doesn’t exist an exception is thrown and the respective catch block is executed. Inside the catch block the method “createDatabase()” is invoked to create the database. This process is performed at least 2 times, since the application properties should be loaded anyway. See the “createDatabase()” method below:

{% highlight java %}
private static void createDatabase() {
  logger.info("Creating the database for the first time");
  List<string> sqlCommands =
    loadSQLCommands(Main.class
            .getResourceAsStream("/META-INF/create-database.sql"));
  EntityManagerFactory emf = Persistence.createEntityManagerFactory(
    AbstractEntity.ENTITY_MANAGER);
  EntityManager em = emf.createEntityManager();
  EntityTransaction et = null;
  String sqlCommand = null;
  try {
    et = em.getTransaction();
    et.begin();
    for(int i = 0;i < sqlCommands.size();i++) {
      sqlCommand = sqlCommands.get(i);
      em.createNativeQuery(sqlCommand).executeUpdate();
      logger.info("database update: " + sqlCommand);
    }
    initializeDatabase(em);
  }
  catch(Exception ex) {
    logger.log(Level.WARNING,
               "Problem to execute the sql command: "+
               sqlCommand, ex);
    et.rollback();
  }
  finally {
    et.commit();
    em.close();
  }
}
{% endhighlight %}

The code above accesses the file `create-database.sql` embedded inside the application jar, extracts a list of sql commands, executes one by one, and initializes the database, inserting some initial default data. I list below the method “loadSQLCommands()” that opens the embedded file and reads its content:

{% highlight java %}
public static List<string> loadSQLCommands(InputStream stream) {
  List<string> sqlCommands = new ArrayList<string>();
  try {
    BufferedReader reader = new BufferedReader(
      new InputStreamReader(stream));
    StringBuffer sb = new StringBuffer();
    String line = null;
    while((line = reader.readLine()) != null) {
      sb.append(line.trim());
    }
    StringTokenizer st = new StringTokenizer(sb.toString(), ";");
    while(st.hasMoreTokens()) {
      sqlCommands.add(st.nextToken());
    }
    return sqlCommands;
  } catch (MalformedURLException ex) {
    logger.log(Level.SEVERE, "Malformed URI of the file.", ex);
  } catch (FileNotFoundException fnfe) {
    logger.log(Level.WARNING, "Database script not found.", fnfe);
  } catch (IOException ioe) {
    logger.log(Level.WARNING, "Problem to read the script.", ioe);
  }
  return null;
}
{% endhighlight %}

Finally, the method ‘initializeDatabase()”, invoked at the end of the method `createDatabase()`, is listed below:

{% highlight java %}
public static void initializeDatabase(EntityManager em) {
  logger.info("Initializing the database"+
              "for the first time.");
  List<string> sqlCommands = loadSQLCommands(
    Main.class.getResourceAsStream("/META-INF/initialize-database.sql"));
  for(String sqlCommand:sqlCommands) {
    em.createNativeQuery(sqlCommand).executeUpdate();
    logger.info("data update: " + sqlCommand);
  }
}
{% endhighlight %}

With all this code above we could solve only the database creation process. There are still more code to update the database when needed. Because this post became so big, I’m going to describe the update process in a future post in this blog. Maybe, I missed some point here because there are so many details. So, if you had problems to implement it, please leave your comments below and I will try to complement the content to fulfill your needs. Keep following me!
