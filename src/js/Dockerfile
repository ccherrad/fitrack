# Dockerfile for Nuxt.js Application
FROM node:18

# Set the working directory
WORKDIR /app

# Copy the package.json and yarn.lock files
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the Nuxt.js app code
COPY . .

# Build the Nuxt.js application
RUN npm run build

# Expose the port Nuxt.js will run on
EXPOSE 3000

# Command to run the application
CMD ["npm", "run", "dev"]
