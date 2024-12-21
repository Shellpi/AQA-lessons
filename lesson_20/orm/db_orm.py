"""Db init."""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker



DB_STRING = 'sqlite:///shop_internet.sqlite'
Base = declarative_base()


class Db:
    """Db ORM class.

    This class encapsulates the database connection and initialization logic
    for managing ORM operations using SQLAlchemy. It sets up the engine,
    session, and metadata required to interact with the database.
    """

    def __init__(self):
        """Initialize the Db class.

        - Creates a database engine based on the DB_STRING.
        - Sets up a scoped session to manage database transactions.
        - Initializes the database schema using the `_init_db` method.
        """
        # Create a database engine to handle the connection to the database.
        # The engine is the starting point for all SQLAlchemy operations.
        self.engine = create_engine(DB_STRING)

        # Set up a scoped session. This session ensures thread-safe handling of
        # database interactions and simplifies transaction management.
        self.session = scoped_session(
            sessionmaker(
                autocommit=False,  # Transactions are explicitly committed to ensure data integrity.
                autoflush=False,  # Prevent automatic flushing of changes to the database.
                bind=self.engine  # Bind the session to the created engine.
            )
        )

        # Initialize the database schema and associate the session with the base query property.
        self._init_db()

    def _init_db(self):
        """Initialize database ORM metadata.

        - Associates the `Base.query` property with the session, enabling query operations
          directly from ORM classes that inherit from the `Base`.
        - Creates all database tables defined by the ORM models (if they do not already exist).
        """
        # Associate the session with the query property of the Base class.
        # This allows ORM models to use the `query` property for database operations.
        Base.query = self.session.query_property()

        # Create all tables defined in the ORM models.
        # If the tables already exist in the database, this operation is a no-op.
        Base.metadata.create_all(bind=self.engine)
