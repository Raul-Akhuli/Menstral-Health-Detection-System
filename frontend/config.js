/**
 * Configuration Manager for Blood Health Advisor
 * Handles environment-specific API base URLs
 */

// ─── ENVIRONMENT DETECTION ──────────────────────
const ENVIRONMENT = {
    LOCAL: {
        name: "local",
        baseUrl: "http://127.0.0.1:8022",
        description: "Local development server"
    },
    PRODUCTION: {
        name: "production",
        baseUrl: "https://server.uemcseaiml.org:8022/blood",
        description: "UEM Server (Production)"
    }
};

// ─── ACTIVE CONFIGURATION ───────────────────────
// MANUALLY TOGGLE WHICH ENVIRONMENT TO USE:
// 1. For local development & testing: Set to ENVIRONMENT.LOCAL
// 2. For production/Vercel deployment: Set to ENVIRONMENT.PRODUCTION
//
// WORKFLOW:
// During Development:
//   - Set to LOCAL, test backend locally
// Before GitHub Push & Vercel Deploy:
//   - Set to PRODUCTION, commit & push
const ACTIVE_ENV = ENVIRONMENT.LOCAL;

// ─── DERIVED CONFIGURATION ──────────────────────
const BASE_URL = ACTIVE_ENV.baseUrl;

// Debug logging (remove in production if needed)
console.log(`🔗 Backend Environment: ${ACTIVE_ENV.name.toUpperCase()} (${ACTIVE_ENV.description})`);
console.log(`📍 Base URL: ${BASE_URL}`);
