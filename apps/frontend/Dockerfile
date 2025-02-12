# Use Node.js base image
FROM node:18

# Set working directory
WORKDIR /apps

# Copy package files and install dependencies
# COPY package.json package-lock.json ./
RUN npm install

# Copy project files
COPY . .

# Expose React app port
EXPOSE 3000

# Start React app
CMD ["npm", "start"]
