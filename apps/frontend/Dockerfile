# Use Node.js base image
FROM node:18

# Set working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json .
COPY package-lock.json .
RUN npm install

# Copy app source code
COPY . .

# Expose port and start app
EXPOSE 3000
# CMD ["npm", "start"]

# Keep container running
CMD ["tail", "-f", "/dev/null"]

# CMD ["npm", "start"]
