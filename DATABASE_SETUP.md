# Database Setup Instructions

## Getting Your Neon PostgreSQL Connection String

1. **Log into your Neon Console**: Go to [console.neon.tech](https://console.neon.tech)

2. **Select your project**: Choose the project you want to use for this application

3. **Get the connection string**:
   - Navigate to your project page
   - Click on "Connection Details" or "Connect" button
   - Select "Python" from the language options
   - Copy the connection string (it should look like: `postgresql+psycopg://username:password@ep-xxxxxx.us-east-1.aws.neon.tech/neondb?sslmode=require`)

4. **Update your .env file**:
   - Open the `.env` file in your project root
   - Replace `your_actual_neon_database_url_here` with your copied connection string

## Initialize the Database Tables

Once you've updated your .env file with the correct database URL, run the following commands:

```bash
# From the project root directory
cd backend
python -c "from src.database import init_db; init_db()"
```

Or alternatively, you can run the application which will automatically initialize the tables on startup.

## Verify Database Connection

You can verify that the tables have been created by:
1. Checking your Neon console dashboard
2. Looking for tables named `user` and `task` in your database schema

## Troubleshooting

If you encounter connection issues:
- Verify your internet connection
- Check that the connection string is correct
- Ensure your Neon project is active and not paused
- Confirm that SSL is enabled in your connection string

For authentication issues, make sure to also update the JWT_SECRET and other required environment variables.